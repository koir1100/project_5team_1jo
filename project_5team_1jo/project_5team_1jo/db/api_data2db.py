import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db.settings')
django.setup()

from books_api import serializer
from books_api.serializer import RecomBooksSerializer

def data2db(data):
    #data: dict 리스트 ex)
    for i in range(len(data)):
        serializer = RecomBooksSerializer(data=data[i])
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)