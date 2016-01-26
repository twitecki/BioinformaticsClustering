import sys
import string
import random
from data import *
from display import *
from comparisons import getEuclideanDistance, getPearsonDistance
from ClusteringSettings import *

def generateKlusterCode():
	letters = string.letters
	c1 = random.choice(letters)
	c2 = random.choice(letters)
	c3 = random.choice(letters)
	c4 = random.choice(letters)
	retString = c1 + c2 + c3 + c4
	return retString

def buildInitialNodeArray(objectArray):
	nodeArray = []
	for arr in objectArray:
		newNode = Node(None, None, 0, arr[0].fm)
		nodeArray.append(newNode)
	return nodeArray

def buildDistanceMatrix(objectArray, distType):
	distanceMatrix = []
	for i in range(0, len(objectArray)):
		matrixColumn = []
		for j in range(0, len(objectArray)):
			#matrixColumn.append(DistanceMeasurement([objectArray[i]], [objectArray[j]], compareObjects(objectArray[i],objectArray[j])))
			if (distType == "Euclidean"):
				matrixColumn.append(DistanceMeasurement([objectArray[i]], [objectArray[j]], getEuclideanDistance(objectArray[i],objectArray[j], 3)))
			elif (distType == "Pearson"):
				matrixColumn.append(DistanceMeasurement([objectArray[i]], [objectArray[j]], getPearsonDistance(objectArray[i],objectArray[j])))
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
	if (DEBUG):
		print location
		print "" 
	return location

def indexOfNode(nodeArray, cluster):
	for i in range(0,len(nodeArray)):
		if str(nodeArray[i].cluster) == str(cluster):
			if (DEBUG):
				print 'Index of ' + str(cluster) + ' is ' + str(i)
			return i
	return -1

def mergeClusters(distArray, nodeArray, isLastRun):
	
	if (isLastRun):

		location = findMergeLocation(distArray)

		newCluster = []
		m3 = distArray[location[0]][location[1]] #The Distance Measure to merge
		
		leftNode = nodeArray[indexOfNode(nodeArray, m3.fm)]
		rightNode = nodeArray[indexOfNode(nodeArray, m3.to)]
		nodeCluster = m3.fm + m3.to	
		n = Node(leftNode, rightNode, m3.distance, nodeCluster)
		nodeArray.append(n)
		if (DEBUG):
			print n.displayNode()
		return ([[]], nodeArray)
	else:
		location = findMergeLocation(distArray)

		newCluster = []
		m3 = distArray[location[0]][location[1]] #The Distance Measure to merge

		leftNode = nodeArray[indexOfNode(nodeArray, m3.fm)]
		rightNode = nodeArray[indexOfNode(nodeArray, m3.to)]
		nodeCluster = m3.fm + m3.to	
		n = Node(leftNode, rightNode, m3.distance, nodeCluster)
		nodeArray.append(n)
		if (DEBUG):
			print n.displayNode()

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
		
		if (DEBUG):
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

		return (newDist, nodeArray)

