import tifffile as tiff
import numpy as np
import os
import fnmatch
import matplotlib.pyplot as plt 
import scipy.ndimage as simg
import skimage as ski

# TODOs :
# this code consideres that the nput images are 8-bits, but it would be more convenient to have a function that checks that. 


def createNewDirectory(directory: str, newFileName: str):
	"""
	Create new folder. 
	Returns the path of the new folder. 
	"""
	newDir = directory+"/"+newFileName
	if not os.path.exists(newDir):
		os.makedirs(newDir)
	return newDir

def listNameOfFiles(directory: str, extension="tif") -> list:
	"""
	Fetch files name. 
	Does not consider .DS_Store files. 
	Returns a list of the names of the files. 
	"""
	foundFiles = []
	for file in os.listdir(directory):
		if fnmatch.fnmatch(file, f'*.{extension}'):
			if file == ".DS_Store":
				pass
			else:
				foundFiles.append(file)
	return foundFiles

def read_file(file_path):
	"""
	Reads the .tif file and convert them in a np.array. 
	Returns the file as a np.array. 
	"""
	image_array = tiff.imread(file_path)
	return image_array


def fix_polygon(image, firstLinePosition):
	"""
	Replaces the black horizontal lines by the average of the value of the pixel
	before and after the pixel in the line. 
	First value in range is the position of the first black line from the top of the image.
	Returns the image as a np.array without the black horizontal line. 
	"""
	for i in range(firstLinePosition, 511, 36):
		image[i] = image[i+1]/2 + image[i-1]/2

	firstLinePosition = firstLinePosition + 8 - 36
	if firstLinePosition < 0:
		firstLinePosition += 36

	for i in range(firstLinePosition, 511, 36):
		image[i] = image[i+1]/2 + image[i-1]/2

	return image

def deleteRowInImage(image, rowsToDelete):
	"""

	"""
	x = 0
	while x < rowsToDelete:
		image = np.delete(image, x, 0)
		x += 1
	print("DEL IMAGE : {}{}".format(image, image.shape[0]))

	return image

def sumPixels(directory:str, filesName):
	"""
	Reads all images in directory and sums the value of each pixels. 
	Returns an image with the sum of all pixels. 
	"""
	firstPath = directory + "/" + filesName[0]
	firstImage = read_file(file_path=firstPath)

	pixels = np.zeros(shape=(firstImage.shape[0], firstImage.shape[1]), dtype=np.float64)

	for name in filesName:
		filePath = directory + "/" + name
		image = read_file(file_path=filePath)
		x = 0
		y = 0
		while x < firstImage.shape[0]:
			while y < firstImage.shape[1]:
				pixels[x][y] = pixels[x][y] + image[x][y]
				y += 1
			y = 0
			x += 1

	return pixels

def normalizeImage(image):
	""" 
	Creates an image with pixels in float 64 varying form 0 to 1 according to the intensity of each pixels from the input image.
	"""
	newImage = np.zeros(shape=(image.shape[0], image.shape[1]))
	maxPixel = np.amax(image)

	x = 0
	y = 0
	while x < image.shape[0]:
		while y < image.shape[1]:
			newImage[x][y] = image[x][y]/maxPixel
			y += 1
		y = 0
		x += 1

	return newImage

def rescaleImage(image, pixelRange=255):
	"""
	Normalizes the image with the function normalizeImage. 
	Rescales the image on the range defined with the variable pixelRange. 
	"""
	normImage = normalizeImage(image=image)
	rescaledImage = np.zeros(shape=(image.shape[0], image.shape[1]))

	x = 0
	y = 0
	while x < image.shape[0]:
		while y < image.shape[1]:
			rescaledImage[x][y] = normImage[x][y] * pixelRange
			y += 1
		y = 0
		x += 1

	return rescaledImage


def inversePixels(image):
	"""
	Takes the input image and inverses the pixels (0s become 1s and 1s become 0s). 
	"""

	inverseImage = np.zeros(shape=(image.shape[0], image.shape[1]))
	maxPixel = np.amax(image)

	x = 0
	y = 0
	while x < image.shape[0]:
		while y < image.shape[1]:
			inverseImage[x][y] = maxPixel - image[x][y]
			y += 1
		y = 0
		x +=1

	return inverseImage

def createAverageImage(directory: str, filesName):
	"""
	With the image directory, averages them all to produce a final image for correction. 
	Returns the resultant average image. 
	"""
	pixels = sumPixels(directory=directory, filesName=filesName)
	numberOfImages = len(filesName)

	x = 0
	y = 0
	while x < pixels.shape[0]:
		while y < pixels.shape[1]:
			pixels[x][y] = pixels[x][y]/numberOfImages 
			y += 1
		y = 0
		x += 1

	return pixels

def averageRowsOfTwoImages(image1, image2, row1, row2): 
	"""
	This function takes two .tif images and average each element according to their row number. 
	If row1 and row2 = 0, the first row of each image are averaged together, element by element. 
	The average finishes when the row of image 1 does not exist anymore. 
	"""
	while row1 < image1.shape[0]:
		rowsToAverage = np.vstack((image1[row1], image2[row2]))
		image1[row1] = np.mean(rowsToAverage)
		row1 += 1
		row2 += 1

	return image1

def createIntensityCorrectionImage(image):
	"""
	From an average image of all images in a set, generates the intensity correction image that should be applied on individual images. 
	Applies a gaussian blur on the correction image to smoothen the stuff. 
	Returns the intensity correction image with values between 0 and 1.
	"""
	inverseImage = inversePixels(image=image)
	rescaledImage = rescaleImage(image=inverseImage)
	correction = simg.gaussian_filter(rescaledImage, sigma=10, mode="nearest")

	return correction

def adjustIntensity(image, correction):
	""" 
	Takes an image and multiplies each pixels by the correcponding pixel in the correction image. 
	Returns the image corrected in intensity. 
	"""
	image = image.astype(np.float64)

	x = 0
	y = 0
	while x < image.shape[0]:
		while y < image.shape[1]: 
			image[x][y] = image[x][y] * correction[x][y]
			y += 1
		y = 0
		x += 1

	new8bitImage = np.uint8(rescaleImage(image))

	# adjust the background for better contrast. Here the background is defined as any pixel under 20. 
	x = 0
	y = 0
	while x < new8bitImage.shape[0]:
		while y < new8bitImage.shape[1]:
			if new8bitImage[x][y] < 20:
				new8bitImage[x][y] = 0
			y += 1
		y = 0
		x += 1

	return new8bitImage


def stitchTwoImagesHorizontal(image1, image2, overlap):
	numberOfOverlapedRows = int(512 * overlap / 100)
	rowImage1 = 512 - numberOfOverlapedRows
	rowImage2 = 0

	averageImage = averageRowsOfTwoImages(image1, image2, row1=rowImage1, row2=rowImage2)

	del_image2 = deleteRowInImage(image=image2, rowsToDelete=numberOfOverlapedRows)
	stitchImage = np.concatenate((image1, del_image2), axis=0) 

	return stitchImage

def stitchTwoImagesVertical(image1, image2, overlap):
	numberOfOverlapedRows = int(1064 * overlap / 100)
	columnImage1 = 1064 - numberOfOverlapedRows
	columnImage2 = 0

	









