#This File contains all information for reading data from txt & csv files
import csv
from data import DataObject

def buildObjectArray(fileName):
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		objArray = []
		for row in reader:
			name = str(row[0])
			values = row[1:len(row)]
			newObject = DataObject(name, values)
			objArray.append(newObject)
		return objArray
