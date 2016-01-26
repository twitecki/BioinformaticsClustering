#TESTING GIT

import sys
import testObjects.py

distances = []

distances.append([   0, 1075, 671, 2684, 2631, 1616])
distances.append([1075,   0, 1329, 3273, 2687, 2037])
distances.append([ 671, 1329,   0, 2013, 2054,  996])
distances.append([2684, 3273, 2013,   0,  808, 1307])
distances.append([2631, 2687, 2054, 808,    0, 1059])
distances.append([1616, 2037,  996,1307, 1059,    0])

for i in range(len(distances)):
	print distances[i]

def findMergeLocation(distArray):
	minimum = sys.maxsize
	location = (0,0)
	for i in range(len(distArray)):
		for j in range(i, len(distArray)):
			if distArray[i][j] != 0 and distArray[i][j] < minimum: 
				minimum = distArray[i][j]
				location = (i,j)
	return location

def mergeClusters(distArray):
	location = findMergeLocation(distArray)

	#doesn't work for case when you are at a 2x2 matrix : fixed almost
	newCluster = []
	for i in range(len(distArray)):
		if i != location[1]:
			if len(distArray) == 2 or distArray[location[1]][i] == 0: #this case deals with all 0's on the 2x2
				newCluster.append(max(distArray[location[0]][i], distArray[location[1]][i]))
			else:
				newCluster.append(min(distArray[location[0]][i], distArray[location[1]][i]))
	
	print "\n"
	print "New Cluster: " 
	print newCluster
	print "\n"

	newDist = []
	numColumns = len(distArray)

	for i in range(0, numColumns - 1):
		newDist.append([])

	for i in range(0, numColumns):
		if i != location[1]:
			if i < location[1]:
				index = i
			elif i > location[1]:
				index = i - 1
			if i == location[0]:
				map(lambda x: newDist[index].append(x), newCluster)
			else:
				for x in range(0, len(distArray[i])):
					
					if x != location[1]:
						if x == location[0]:
							value = newCluster[index]
							newDist[index].append(value)
						else:
							value = distArray[i][x]
							newDist[index].append(value)

	return newDist

test = distances
print findMergeLocation(test)
test = mergeClusters(test)
test = mergeClusters(test)
test = mergeClusters(test)
test = mergeClusters(test)
#print findMergeLocation(test)

for i in range(len(test)):
	print test[i]

