from data import *
import io

def createJSONString(root):
	jsonString = ""
	jsonString += '{\n'
	jsonString += '\t\"name\": \"root\", \"y\" : 0,\n'
	jsonString += '\t\"children\": [\n'
	#fStream.write('\t{\n')
	jsonStringHelper(jsonString, root.left, root.distance)
	jsonString += '\t,'
	jsonStringHelper(jsonString, root.right, root.distance)
	#fStream.write('\t}\n')
	jsonString += '\t]\n'
	jsonString += '}'
	return 	jsonString

def jsonStringHelper(jsonString, node, rDist):
	if (node != None):
		#if the node is a leaf node, end the bracket
		if (node.left == None and node.right == None):
			outString = '\t\t{"name\": \"' + str(node.cluster) + '\", \"y\" : ' + str((rDist - node.distance)) + '}'
			jsonString += outString
		else:
			jsonString += '\t{\n'
			outString = '\t\t\"name\": \"' + str(node.cluster) + '\", \"y\" : ' + str((rDist - node.distance)) + ',\n'
			fjsonString +=(outString)
			jsonString += '\t\t\"children\": [\n'
			jsonStringHelper(jsonString, node.left, rDist)
			jsonString += ',\n'
			jsonStringHelper(jsonString, node.right, rDist)
			jsonString += '\t]\n'
			jsonString += '\t}\n'
