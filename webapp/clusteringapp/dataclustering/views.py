from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core import serializers

from django.template.loader import get_template
from django.template import Context

from clustering_code.run import buildJSONTree, generateKlusterCode
from clustering_code.utilities import *
import threading
import Queue
from dataclustering.models import Kluster, KlusterUser

# Create your views here.
def home_view(request):
	t = get_template('home.html')	
	html = t.render(Context())
	return HttpResponse(html)

def make_kluster_view(request):
	t = get_template('makeKluster.html')
	c = {}
	c.update(csrf(request))
	html = t.render(Context())
	return render_to_response('makeKluster.html', c)

def instructions_view(request):
	t = get_template('instructions.html')
	html = t.render(Context())
	return HttpResponse(html)

def insertcode_view(request):
	t = get_template('insertcode.html')
	html = t.render(Context())
	return HttpResponse(html)

def myKlusters_view(request):
	t = get_template('myklusters.html')	
	f = None
	if request.method == 'POST':
		f = request.FILES['file']
		distType = request.POST['distanceMetric']
		if f:
			jsonString = buildJSONTree(f, distType)
			#Validate JSON String here
			#if (isValid jsonString)
			#Generate Code to store in database
			unique = False
			klusterKode = ""
			while (not unique):
				klusterKode = generateKlusterCode()
				count = Kluster.objects.filter(code=klusterKode).count()
				if (count == 0):
					unique = True

			Kluster.objects.create(code=klusterKode, JSON=jsonString, distanceMetric=distType)
        	return render(request, 'myklusters.html', {'file': f})
        else:
		#contentOfFile = file1.read()
		#context = Context(['filename' : ])
			html = t.render(Context())
			return HttpResponse(html)

def getjsonfromcode(request):
	requestCode = ""
	if request.method == 'GET':
		requestCode = request.GET['code']
	k = Kluster.objects.get(code=requestCode)
	tempObj = serializers.serialize("json", [k])
	jsonObj = tempObj[1:-1]
	return HttpResponse(jsonObj)

def createkluster(request):
	f = None
	if request.method == 'POST':
		try:
			f = request.FILES['file']
			distType = request.POST['distanceMetric']
		except:
			return HttpResponse("noFile")
		if f:
			q = Queue.Queue()
			t1 = threading.Thread(target=buildJSONTree, args=(f, distType, q))
			t1.start()
			t1.join(30.0)
			if t1.isAlive():
				return HttpResponse("timeout")
			else:
				jsonString = q.get()
				if is_json(jsonString):
					#jsonString = buildJSONTree(f, distType)

					#Validate JSON String here
					#if (isValid jsonString)
					#Generate Code to store in database
					unique = False
					klusterCode = ""
					while (not unique):
						klusterCode = generateKlusterCode()
						count = Kluster.objects.filter(code=klusterCode).count()
						if (count == 0):
							unique = True

					Kluster.objects.create(code=klusterCode, JSON=jsonString, distanceMetric=distType)
					objToSerialize = Kluster.objects.get(code=klusterCode)
					tempObj = serializers.serialize("json", [objToSerialize])
					jsonObj = tempObj[1:-1]
					return HttpResponse(jsonObj)
				else:
					return HttpResponse("fileError")
	else:
		return HttpResponse("Not a POST request")