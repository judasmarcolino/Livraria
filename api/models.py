from django.db import models

# Create your models here.

class Livro():
    titulo = models.CharField(max_length=50)

