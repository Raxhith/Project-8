from django.shortcuts import render
from django.http import HttpResponse

def nat_gam(request):
	data = '<h1>The national game is HOCKEY</h1>'
	return HttpResponse(data)

def nat_ani(request):
	data = '<h1>The national animal is TIGER</h1>'
	return HttpResponse(data)

def nat_flo(request):
	data = '<h1>The national flower is LOTUS</h1>'
	return HttpResponse(data)
