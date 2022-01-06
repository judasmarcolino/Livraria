
from django.urls import path
from . import views



urlpatterns = [
    path('',views.inicio, name="inicio"),

    path('',views.index, name="index")

]
