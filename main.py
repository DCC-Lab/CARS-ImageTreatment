from functions import *

sourcePath = "/Users/valeriepineaunoel/Desktop/20220621-6umPolystyreneBeads-overlap10%-zoom2/LineCorrection"
firstLine = 35
overlap = 31
tileDimensions = [6, 4] #number of images 

#Step 1 : Average horizontal lines generated from scratches on pylogon mirror 
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
## Vertical stitching 

files = listNameOfFiles(directory=sourcePath)
stitchingPath = createNewDirectory(directory=sourcePath, newFileName="Vertical Stitching")

x = 0
verticalStitching = 1
while x < tileDimensions[0]:
	y = 0

	j = x
	topFilePath = sourcePath + "/" + files[j]
	topImage = read_file(file_path=topFilePath)
	y += 1

	j += tileDimensions[0]
	secondTopFilePath = sourcePath + "/" + files[j]
	secondTopImage = read_file(file_path=secondTopFilePath)
	y += 1

	# The first image is now going to be the first and the second images stitched together
	stitchImage = stitchTwoImagesVertical(image1=topImage, image2=secondTopImage, overlap=overlap)

	# For each following images, stitches them to the first image (who already has the second and first images stitched)
	while y < tileDimensions[1]:
		j += tileDimensions[0]
		path = sourcePath + "/" + files[j]
		image = read_file(file_path=path)
		stitchImage = stitchTwoImagesVertical(image1=stitchImage, image2=image, overlap=overlap)
		y += 1
	tiff.imwrite(stitchingPath + str(verticalStitching) + ".tif", stitchImage)
	verticalStitching += 1
	x += 1

## Horizontal stitching





