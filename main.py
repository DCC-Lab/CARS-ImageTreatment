from functions import *

sourcePath = "/Users/valeriepineaunoel/Desktop/20220621-6umPolystyreneBeads-overlap10%-zoom2/LineCorrection"
firstLine = 35
overlap = 10
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
#destinationStitchingPath = createNewDirectory(directory=sourcePath, newFileName="StitchXY")

files = listNameOfFiles(directory=sourcePath)

i = 0
y = 0

#while y < tileDimensions[1]:
print(i)
topFilePath = sourcePath + "/" + files[i]
topImage = read_file(file_path=topFilePath)
tiff.imwrite("/Users/valeriepineaunoel/Desktop/" + str(i) + ".tif", topImage)
i += tileDimensions[0]

secondTopFilePath = sourcePath + "/" + files[i]
secondTopImage = read_file(file_path=secondTopFilePath)
tiff.imwrite("/Users/valeriepineaunoel/Desktop/" + str(i) + ".tif", secondTopImage)
i += tileDimensions[0]
print(i)

stitchedImage = stitchTwoImagesVertical(image1=topImage, image2=secondTopImage, overlap=overlap)
	
y += 2
	#while y < tileDimensions[1]:
	#	path = sourcePath + "/" + files[i]
	#	image = read_file(file_path=path)
	#	stitchedImage = stitchTwoImagesVertical(image1=stitchedImage, image2=image, overlap=overlap)
	#	y += 1
	#	i += 1
tiff.imwrite("/Users/valeriepineaunoel/Desktop/" + str(i) + ".tif", stitchedImage)
	

# RESTE À FAIRE LE STITCHING VERTICAL LES AMIS


#filePath1 = sourcePath + "/" + files[0]
#filePath2 = sourcePath + "/" + files[1]
#image1 = read_file(file_path=filePath1)
#image2 = read_file(file_path=filePath2)
#stitchTwoImagesHorizontal(image1, image2, overlap)

