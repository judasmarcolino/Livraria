from django.shortcuts import render, render_to_response

from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1> Ola </h1>")

def index(request):
    return render(request, 'paginas/ index.html')