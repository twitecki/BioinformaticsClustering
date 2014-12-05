#Object to be clustered
class DataObject: 
	def __init__(self, name, values):
		self.name = name
		self.values = values
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name


#Two clusters (from and to) and the distance between the two clusters
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
		return "fm:" + str(self.fm) + " to:" + str(self.to) + " " + str(self.distance)

class Node:
	def __init__(self, left, right, distance, cluster):
		self.left = left
		self.right = right
		self.distance = distance
		self.cluster = cluster
	def __str__(self):
		return str(self.cluster)
	def __repr__(self):
		return str(self.cluster)
	def displayNode(self):
		print 'L: ' + str(self.left) + ' R: ' + str(self.right) + ' D: ' + str(self.distance) + ' C: ' + str(self.cluster)
