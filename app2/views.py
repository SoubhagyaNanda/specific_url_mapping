from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<marquee><h1> This Is Sample1 of app2 </h1></marquee>')

def second(request):
    return HttpResponse('<marquee><h1> This Is Sample2 Of app2 </h1></marquee>')