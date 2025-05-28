from django.db import models

# Create your models here.

class Contatto(models.Model):
    nome = models.CharField(max_length=100,blank=True)
    cognome = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    contenuto = models.TextField(blank=True)