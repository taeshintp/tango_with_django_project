from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says hey there partner!")
    return HttpResponse('<a href="about">Rango says hey there partner!</a>')
    

def rango(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page.")
    return render(request, 'rango/about.html')