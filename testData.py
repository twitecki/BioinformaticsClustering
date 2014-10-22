import sys
from testObjects import *
from clustering import *

object1 = DataObject(["A"], 12)
object2 = DataObject(["B"], 17)
object3 = DataObject(["C"], 6)
object4 = DataObject(["D"], 24)
objects = [object1, object2, object3, object4]

test = buildDistanceMatrix(objects)
printDistanceMatrix(test)
test = mergeClusters(test)
printDistanceMatrix(test)
test = mergeClusters(test)
printDistanceMatrix(test)

print getToFromString(test[1][0].fm)
print getToFromString(test[1][0].to)
