from django.shortcuts import render, render_to_response

from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def livros(request):
    return render(request, 'livros/index.html')

def cadastrar(request):
    return render (request, 'livros/cadastro.html')
def editar(request):
    return render (request, 'livros/editar.html')
def eliminar(request):
    return render (request, 'livros/eliminar.html')
