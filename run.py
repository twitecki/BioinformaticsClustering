import sys
from data import *
from comparisons import *
from clustering import *
from testFunctions import *
from display import *

def findAnswer(matrix):
	while(len(matrix) > 2):
		printDistanceMatrix(matrix)
		matrix = mergeClusters(matrix)
	printDistanceMatrix(matrix)

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


#da = readDistancesFromFile('TestTextFiles/test1.txt')
#da = readDistancesFromFile('TestTextFiles/test2.txt')
try :
	da = readDistancesFromFile(sys.argv[1])
	test = buildTestDistanceMatrix(da)
	findAnswer(test)
except IOError:
	print "File not found"




