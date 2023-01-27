from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    pass
    #return HttpResponse("Rango says hey there partner!")
    return HttpResponse('<a href="about">Rango says hey there partner!</a>')


def about(request):
    #return HttpResponse("Rango says here is the about page.")
    return HttpResponse('<a href="/">Rango says here is the about page.</a>')