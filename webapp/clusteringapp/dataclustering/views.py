from django.shortcuts import render
from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context

# Create your views here.
def home_view(request):
	t = get_template('home.html')	
	html = t.render(Context())
	return HttpResponse(html)

def make_kluster_view(request):
	t = get_template('makeKluster.html')	
	html = t.render(Context())
	return HttpResponse(html)

def instructions_view(request):
	t = get_template('instructions.html')	
	html = t.render(Context())
	return HttpResponse(html)

def myKlusters_view(request):
	t = get_template('myklusters.html')	
	html = t.render(Context())
	return HttpResponse(html)
