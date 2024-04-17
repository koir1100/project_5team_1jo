from django.db import models

# Create your models here.

class Book(models.model):
    recomNum = models.CharField(max_length=200)