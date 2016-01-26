import math

#Basic comparison function for testing
def compareObjects(obj1, obj2):
	return abs(obj1.value - obj2.value)

def getEuclideanDistance(obj1, obj2, precision):
	valueArr1 = obj1.values
	valueArr2 = obj2.values
	acc = 0
	for i in range(len(valueArr1)):
		v1 = 0
		v2 = 0
		try:
			v1 = float(valueArr1[i]) * 10
		except ValueError:
			v1 = 0
		try:
			v2 = float(valueArr2[i]) * 10
		except ValueError:
			v2 = 0
		acc += (v1 - v2)**2
	return round(math.sqrt(acc), precision)

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(arr1, arr2):
    assert len(arr1) == len(arr2)
    x = []
    y = []
    for i in range(len(arr1)):
    	x.append(float(arr1[i]))
    	y.append(float(arr2[i]))
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

def distance_from_pearson(corr):
    return 1 - corr

def getPearsonDistance(obj1, obj2):
	return distance_from_pearson(pearson_def(obj1.values, obj2.values))