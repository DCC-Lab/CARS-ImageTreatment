from functions import *

sourcePath = "/Users/valeriepineaunoel/Desktop/testImages"
firstLine = 35
overlap = 10
tileDimension = [4, 6]

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

#files = listNameOfFiles(directory=destinationLinePath)
#pathFirstImage = destinationLinePath + "/" + files[0]
#firstImage = read_file(file_path=pathFirstImage)
#
#i = 1
#while i < len(files):
#	for x in tileDimension[0]:
#		for y in tileDimension[1]:
#			filePath = sourcePath + "/" + files[i]
#			image = read_file(file_path=filePath)
#			firstImage = stitchTwoImagesHorizontal(image1=firstImage, image2=image, overlap=overlap)
#			i += 1

filePath1 = sourcePath + "/" + files[0]
filePath2 = sourcePath + "/" + files[1]
image1 = read_file(file_path=filePath1)
image2 = read_file(file_path=filePath2)
stitchTwoImagesHorizontal(image1, image2, overlap)

