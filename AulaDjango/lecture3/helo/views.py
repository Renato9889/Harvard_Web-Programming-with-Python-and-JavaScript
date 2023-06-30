from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "helo/index.html")

def paulo(request):
    return HttpResponse("Hello, Paulo!")

def renato(request):
    return HttpResponse("Hello, Renato!")

def greet(request, name):
    return render(request, "helo/greet.html",{
        "name": name.capitalize()
    })