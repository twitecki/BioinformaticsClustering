import json
import threading


def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except ValueError, e:
		return False
	return True

 
class FuncThread(threading.Thread):
	def __init__(self, target, *args):
		self._target = target
		self._args = args
		threading.Thread.__init__(self)
 
	def run(self):
		self._target(*self._args)