from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LPU(req):
    return HttpResponse("LPU is the best University")
def about(req):
    return HttpResponse("wowowowow")