from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<marquee><h1> This Is Sample1 Of app1 </h1></marquee>')

def second(request):
    return HttpResponse('<marquee><h1> This Is Sample2 Of app1 </h1></marquee>')