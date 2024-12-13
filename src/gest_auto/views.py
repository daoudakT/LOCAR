from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def gestion_auto(request):
    return HttpResponse('<h1> bonjour </h1>')
