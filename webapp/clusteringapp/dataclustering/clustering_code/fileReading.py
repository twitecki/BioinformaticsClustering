#This File contains all information for reading data from txt & csv files
import csv
from data import DataObject

def buildObjectArray(fileInput):
	#f =  fileInput.open('rb')
	fileContent =  fileInput.read()
	lines = fileContent.splitlines()
	reader = csv.reader(lines)
	objArray = []
	for row in reader:
		name = str(row[0])
		values = row[1:len(row)]
		newObject = DataObject(name, values)
		objArray.append(newObject)
	return objArray
