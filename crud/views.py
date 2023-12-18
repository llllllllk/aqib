from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def aqib (request):
    return HttpResponse ("hello aqib")

def saqib (request):
    return HttpResponse ("hello saqib")