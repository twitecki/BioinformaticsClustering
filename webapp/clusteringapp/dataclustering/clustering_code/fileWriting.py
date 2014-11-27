from data import *
import io

def createJSON(fileName, root):
	fStream = io.open(fileName, 'w')
	fStream.write(u'{\n')
	fStream.write(u'\t\"name\": \"root\", \"y\" : 0,\n')
	fStream.write(u'\t\"children\": [\n')
	#fStream.write('\t{\n')
	jsonHelper(fStream, root.left, root.distance)
	fStream.write(u'\t,')
	jsonHelper(fStream, root.right, root.distance)
	#fStream.write('\t}\n')
	fStream.write(u'\t]\n')
	fStream.write(u'}')
	fStream.close()
	return 	

def jsonHelper(fStream, node, rDist):
	if (node != None):
		#if the node is a leaf node, end the bracket
		if (node.left == None and node.right == None):
			outString = unicode('\t\t{"name\": \"' + str(node.cluster) + '\", \"y\" : ' + str((rDist - node.distance)) + '}')
			fStream.write(outString)
		else:
			fStream.write(u'\t{\n')
			outString = unicode('\t\t\"name\": \"' + str(node.cluster) + '\", \"y\" : ' + str((rDist - node.distance)) + ',\n')
			fStream.write(outString)
			fStream.write(u'\t\t\"children\": [\n')
			jsonHelper(fStream, node.left, rDist)
			fStream.write(u',\n')
			jsonHelper(fStream, node.right, rDist)
			fStream.write(u'\t]\n')
			fStream.write(u'\t}\n')
