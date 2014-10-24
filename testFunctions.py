from data import *

#Returns distance matrix from file without objects
def readDistancesFromFile(fileName):
	file = open(fileName, 'r')
	fileString = file.read()	
	lines = fileString.split('\n')
	distArr = []
	for i in range(0, len(lines)-1):
		distArr.append([])
	for i in range(0, len(lines)-1):
		#nums = lines[i].split(' ')
		nums = lines[i].split('\t')
		for x in range(0, len(nums)):
			distArr[i].append(nums[x])
	return distArr

#Builds objects for distance matrix computed in readDistancesFromFile
#returns a testable distance matrix 
def buildTestDistanceMatrix(testDistanceArray):
	distanceMatrix = []
	for i in range(0, len(testDistanceArray)):
		matrixColumn = []
		for j in range(0, len(testDistanceArray)):
			ch = chr(ord('A') + i)
			f = DataObject(ch, 0)	# From
			t = DataObject(chr(ord('A') + j), 0)	# To
			matrixColumn.append(DistanceMeasurement([f], [t], int(testDistanceArray[i][j])))
		distanceMatrix.append(matrixColumn)
	return distanceMatrix

