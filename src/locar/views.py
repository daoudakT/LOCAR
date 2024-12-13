from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    
    return render(request, "locar/index.html", {})
    # return HttpResponse('<h1> Bienvenue à LOCAR</h1> <p> la meilleure application de location et de gestion de voiture !</p>')