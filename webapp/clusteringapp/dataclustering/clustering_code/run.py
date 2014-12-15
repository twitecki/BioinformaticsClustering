import sys
import os
from data import *
from comparisons import *
from clustering import *
from testFunctions import *
from display import *
from fileWriting import *
from jsonStringWriting import *
from fileReading import *
from ClusteringSettings import *

def findAnswer(matrix, nodeArray):
	nArray = nodeArray
	while(len(matrix) > 2):
		if (DEBUG):
			printDistanceMatrix(matrix)
		result = mergeClusters(matrix, nArray,False)
		matrix = result[0]
		nArray = result[1]

	if (DEBUG):
		printDistanceMatrix(matrix)
		print nArray

	result = mergeClusters(matrix, nArray,True)
	nArray = result[1]
	if (DEBUG):
		print nArray

	return nArray[len(nArray)-1]

#WORKING IMPLEMENTATION
#object1 = DataObject("A", 12)
#object2 = DataObject("B", 17)
#object3 = DataObject("C", 6)
#object4 = DataObject("D", 24)
#objects = [object1, object2, object3, object4]

#object1 = DataObject("A", 3)
#object2 = DataObject("B", 8)
#object3 = DataObject("C", 15)
#object4 = DataObject("D", 11)
#object5 = DataObject("E", 5)
#objects = [object1, object2, object3, object4, object5]


#mt1 = DistanceMeasurement([object1, object2], [object1, object2], 0)
#mt2 = DistanceMeasurement([object2, object3], [object2, object3], 0)
#testMatrix = []
#testMatrix.append(mt1)
#testMatrix.append(mt2)
#printCluster(testMatrix)

def buildJSONTree(inputFile, dType):
	objectArray = buildObjectArray(inputFile)
	distanceMatrix = buildDistanceMatrix(objectArray, dType)
	nodeArray = buildInitialNodeArray(distanceMatrix)
	root = findAnswer(distanceMatrix, nodeArray)
	#fileLocation = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../clusteringapp/static/dendro.json'))
	return createJSONString(root)


#da = readDistancesFromFile('TestTextFiles/test1.txt')
#da = readDistancesFromFile('TestTextFiles/test2.txt')
def printTree(node):
	if (node == None):
		return
	else:
		node.displayNode()
		print ''
		printTree(node.left)
		printTree(node.right)	
		return

try :
	da = readDistancesFromFile(sys.argv[1])
	test = buildTestDistanceMatrix(da)
	nodeArray = buildInitialNodeArray(test)
	root = findAnswer(test, nodeArray)
	if (DEBUG):
		print ''
		printTree(root)
	createJSON(str(sys.argv[2]), root)
except IOError:
	print "File not found"
except IndexError:
	print "Enter a file name to run"
