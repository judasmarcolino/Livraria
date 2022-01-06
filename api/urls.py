
from django.urls import path
from . import views



urlpatterns = [
    path('',views.inicio, name="inicio"),
 
    path('livros',views.livros, name="livros"),
    path("cadastrar",views.cadastrar, name="cadastrar"),
    path("editar",views.editar, name="editar"),
    path("eliminar",views.eliminar, name="eliminar"),


]
