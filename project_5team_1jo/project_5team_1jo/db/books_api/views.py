from django.shortcuts import render
from rest_framework.decorators import api_view
from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from rest_framework.response import Response
from rest_framework import generics

#POST(생성), GET(로드)
class BookList(generics.ListCreateAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer

#PUT(갱신), DELETE(삭제)
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer