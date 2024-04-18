from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#from . import permissions as api_permissions

#POST(생성), GET(로드)
class BookList(generics.ListCreateAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#PUT(갱신), DELETE(삭제)
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookSpecific(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, code):
        books = RecomBooks.objects.filter(drcode=code)
        serializer = RecomBooksSerializer(books, many = True)
        return Response(serializer.data)