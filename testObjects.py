class DataObject:
	def __init__(self, name, value):
		self.name = name
		self.value = value
	def __str__(self):
		return str(self.name)

class DistanceMeasurement: 
	def __init__(self, fm, to, distance):
		self.fm = fm 
		self.to = to 
		self.distance = distance 

	def display(self):
		print "From: " + self.fm + " To: " + self.to + " Distance: " + str(self.distance)
	
	def displayTo(self):
		print str(self.to)

	def displayFm(self):
		print (self.fm)

	def __str__(self):
		#return str(self.fm) + " " + str(self.to) + " " + str(self.distance)
		return str(self.distance)

def compareObjects(obj1, obj2):
	return abs(obj1.value - obj2.value)

def buildDistanceMatrix(objectArray):
	distanceMatrix = []
	for i in range(0, len(objectArray)):
		matrixColumn = []
		for j in range(0, len(objectArray)):
			matrixColumn.append(DistanceMeasurement([objectArray[i]], [objectArray[j]], compareObjects(objectArray[i],objectArray[j])))
		distanceMatrix.append(matrixColumn)

	return distanceMatrix

def printDistanceMatrix(matrix):
	for i in range (0, len(matrix)):
		print "[",
		for j in range(0, len(matrix[i]) - 1):
 			print str(matrix[i][j]) + ", ",
 		print str(matrix[i][j+1]),
		print "]"

def printCluster(cluster):
	print "[",
	for i in range (0, len(cluster) - 1):
		print(cluster[i]),
	print str(cluster[len(cluster)-1]) + "]"

def getToFromString(arr):
	s = ""
	s += "["
	for i in range (0, len(arr) - 1):
		s += str(arr[i])
	s += str(arr[len(arr)-1]) + "]"
	return s

