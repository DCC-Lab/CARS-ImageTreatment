from functions import *

sourcePath = "/Users/valeriepineaunoel/Desktop/testImages"
firstLine = 35
overlap = 10
tileDimensions = [2, 3]

#Step 1 : Average horizontal lines from pylogon
#destinationLinePath = createNewDirectory(directory=sourcePath, newFileName="LineCorrection")
#
#files = listNameOfFiles(directory=sourcePath)
#for file in files:
#	filePath = sourcePath + "/" + file
#	image = read_file(file_path=filePath)
#	imageCorrected = fix_polygon(image=image, firstLinePosition=firstLine)
#	newFileName = destinationLinePath + "/" + "CORR" + file
#	tiff.imwrite(newFileName, imageCorrected)

#Step 2 : Rescale intensity of images from Gaussian envelop. 
#correctorsPath = createNewDirectory(directory=sourcePath, newFileName="AverageAndIntensityCorrectionImages")
#files = listNameOfFiles(directory=destinationLinePath)
#
#aveImage = createAverageImage(directory=destinationLinePath, filesName=files)
#pathAve = correctorsPath + "/" + "Average"
#tiff.imsave(pathAve, aveImage)
#correctionImage = createIntensityCorrectionImage(image=aveImage)
#correctionName = correctorsPath + "/" + "IntensityCorrection"
#tiff.imwrite(correctionName, correctionImage)
#
#pathAfterCorrection = createNewDirectory(directory=sourcePath, newFileName="IntensityAndLineCorrection")
#	
#for file in files:
#	path = destinationLinePath + "/" + file 
#	image = read_file(file_path=path)
#	correctedImage = adjustIntensity(image=image, correction=correctionImage)
#	newFileName = pathAfterCorrection + "/" + "ADJ" + file 
#	tiff.imwrite(newFileName, correctedImage)

#Step 3 : Stitching in x and y from line-corrected images
#destinationStitchingPath = createNewDirectory(directory=sourcePath, newFileName="StitchXY")

files = listNameOfFiles(directory="/Users/valeriepineaunoel/Desktop/testImages")

i = 0
x = 0

while x < tileDimensions[0]:
	topFilePath = "/Users/valeriepineaunoel/Desktop/testImages" + "/" + files[i]
	secondTopFilePath = "/Users/valeriepineaunoel/Desktop/testImages" + "/" + files[i+1]
	i += 2

	topImage = read_file(file_path=topFilePath)
	secondTopImage = read_file(file_path=secondTopFilePath)
	stitchedImage = stitchTwoImagesHorizontal(image1=topImage, image2=secondTopImage, overlap=overlap)
	
	y = 2 
	while y < tileDimensions[1]:
		path = "/Users/valeriepineaunoel/Desktop/testImages" + "/" + files[i]
		image = read_file(file_path=path)
		stitchedImage = stitchTwoImagesHorizontal(image1=stitchedImage, image2=image, overlap=overlap)
		y += 1
		i += 1
	tiff.imwrite("/Users/valeriepineaunoel/Desktop/" + str(i) + ".tif", stitchedImage)
	x += 1


#filePath1 = sourcePath + "/" + files[0]
#filePath2 = sourcePath + "/" + files[1]
#image1 = read_file(file_path=filePath1)
#image2 = read_file(file_path=filePath2)
#stitchTwoImagesHorizontal(image1, image2, overlap)

