class DataObject:
	def __init__(self, name, value):
		self.name = name
		self.value = value
	#def __str__(self):
		#return str(self.name)
	#def __repr__(self):
		#return str(self.name)
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


class DistanceMeasurement: 
	def __init__(self, fm, to, distance):
		self.fm = fm 
		self.to = to 
		self.distance = distance 

	def display(self):
		print "From: " + str(self.fm) + " To: " + str(self.to) + " Distance: " + str(self.distance)
	
	def displayTo(self):
		print str(self.to)

	def displayFm(self):
		print (self.fm)

	def __str__(self):
		#return str(self.fm) + " " + str(self.to) + " " + str(self.distance)
		return "fm:" + str(self.fm) + " to:" + str(self.to) + " " + str(self.distance)
		#return str(self.distance)

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
	for i in range (0, len(matrix)):
		print ''
		for j in range (0, len(matrix[i])):
			print str(matrix[i][j].distance) + "\t",
	print""

def printToFromMatrix(matrix):
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
	if (len(arr) != 0):
			  s = ""
			  s += "["
			  for i in range (0, len(arr) - 1):
				  s += str(arr[i])
			  s += str(arr[len(arr)-1]) + "]"
			  return s

def buildTestDistanceArray(fileName):
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

