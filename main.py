from functions import *

# Initialize variables 
sourcePath = "/Users/valeriepineaunoel/Desktop/20220321-2017ACCSampleImaging/20220321-SpinalCord-AzideTest/20220321-SpinalCord7"
firstLine = 1

destinationLinePath = createNewDirectory(directory=sourcePath, newFileName="LineCorrection")

files = listNameOfFiles(directory=sourcePath)
for file in files:
	filePath = sourcePath + "/" + file
	image = read_file(file_path=filePath)
	imageCorrected = fix_polygon(image=image, firstLinePosition=firstLine)
	newFileName = destinationLinePath + "/" + "CORR" + file
	tiff.imsave(newFileName, imageCorrected)

correctorsPath = createNewDirectory(directory=sourcePath, newFileName="AverageAndIntensityCorrectionImages")
files = listNameOfFiles(directory=destinationLinePath)

aveImage = createAverageImage(directory=destinationLinePath, filesName=files)
pathAve = correctorsPath + "/" + "Average"
tiff.imsave(pathAve, aveImage)
correctionImage = createIntensityCorrectionImage(image=aveImage)
print(correctionImage)
correctionName = correctorsPath + "/" + "IntensityCorrection"
tiff.imsave(correctionName, correctionImage)

pathAfterCorrection = createNewDirectory(directory=sourcePath, newFileName="IntensityAndLineCorrection")
	
for file in files:
	path = destinationLinePath + "/" + file 
	image = read_file(file_path=path)
	correctedImage = adjustIntensity(image=image, correction=correctionImage)
	newFileName = pathAfterCorrection + "/" + "ADJ" + file 
	tiff.imsave(newFileName, correctedImage)
