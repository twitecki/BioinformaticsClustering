import sys
from data import *
from display import *

def buildDistanceMatrix(objectArray):
	distanceMatrix = []
	for i in range(0, len(objectArray)):
		matrixColumn = []
		for j in range(0, len(objectArray)):
			matrixColumn.append(DistanceMeasurement([objectArray[i]], [objectArray[j]], compareObjects(objectArray[i],objectArray[j])))
		distanceMatrix.append(matrixColumn)

	return distanceMatrix

def findMergeLocation(distArray):
	minimum = sys.maxsize
	location = (0,0)
	minMeasurement = []
	for i in range(len(distArray)):
		for j in range(i, len(distArray)):
			if distArray[i][j].distance != 0 and distArray[i][j].distance < minimum: 
				minimum = distArray[i][j].distance
				minMeasurement = DistanceMeasurement(distArray[i][j].fm, distArray[i][j].to, distArray[i][j].distance)
				location = (i,j)
	
	print location
	print "" 
	return location

def mergeClusters(distArray):
	location = findMergeLocation(distArray)

	newCluster = []
	m3 = distArray[location[0]][location[1]] #The Distance Measure to merge
	mergedFrom = m3.fm + m3.to
	for i in range(len(distArray)):
		if i != location[1]:
			if len(distArray) == 2 or distArray[location[1]][i].distance == 0: #this case deals with all 0's on the 2x2
				m1 = distArray[location[0]][i]
				m2 = distArray[location[1]][i]
				newFrom = m1.fm + m2.fm
				if i == location[0]:
					newCluster.append(DistanceMeasurement(mergedFrom, mergedFrom, min(m1.distance, m2.distance)))
				else:
					newCluster.append(DistanceMeasurement(mergedFrom, m1.to, min(m1.distance, m2.distance)))
			else:
				m1 = distArray[location[0]][i]
				m2 = distArray[location[1]][i]
				newFrom = m1.fm + m2.fm
				if i == location[0]:
					newCluster.append(DistanceMeasurement(mergedFrom, mergedFrom, min(m1.distance, m2.distance)))
				else:
					newCluster.append(DistanceMeasurement(mergedFrom, m1.to, min(m1.distance, m2.distance)))
	
	print "NEW CLUSTER: "
	printCluster(newCluster)	
	print ""

	newDist = []
	numColumns = len(distArray)

	for i in range(0, numColumns - 1):
		newDist.append([])

	for r in range(0, numColumns):
		if r != location[1]:
			rowToInsertAt = r
			if r > location[1]:
				rowToInsertAt = r - 1
			if r == location[0]:
				map(lambda x: newDist[rowToInsertAt].append(x), newCluster)
			else:
				for c in range(0, len(distArray[r])):
					if c != location[1]:
						columnToInsertAt = c	
						if c > location[1]:
							columnToInsertAt = c - 1
						if c == location[0]:
							curval = distArray[r][c]
							newTo = distArray[location[0]][location[1]].fm + distArray[location[0]][location[1]].to
							value = DistanceMeasurement(curval.fm, newTo, newCluster[rowToInsertAt].distance)
							newDist[rowToInsertAt].append(value)
						else:
							value = distArray[r][c]
							newDist[rowToInsertAt].append(value)

	return newDist

