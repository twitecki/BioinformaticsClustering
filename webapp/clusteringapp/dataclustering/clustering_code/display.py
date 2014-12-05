from data import *

#Prints distance matrix
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

#Prints the from/to matrix
def printToFromMatrix(matrix):
	for i in range (0, len(matrix)):
		print "[",
		for j in range(0, len(matrix[i]) - 1):
 			print str(matrix[i][j]) + ", ",
 		print str(matrix[i][j+1]),
		print "]"

#Prints an individual cluster
def printCluster(cluster):
	print "[",
	for i in range (0, len(cluster) - 1):
		print(cluster[i]),
	print str(cluster[len(cluster)-1]) + "]"

