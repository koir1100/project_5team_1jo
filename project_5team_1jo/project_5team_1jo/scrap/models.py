from django.db import models

# Create your models here.

class Book(models.Model):
    recomNum = models.CharField(max_length=200)