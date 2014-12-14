from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from django.template.loader import get_template
from django.template import Context

from clustering_code.run import buildJSONTree
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
    	if f:
    		buildJSONTree(f)
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
	jsonString = k.JSON
	return HttpResponse(jsonString)