from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from books_api.serializer import RecomBooksDetailSerializer
from rest_framework import generics, permissions
#from . import permissions as api_permissions

#POST(생성), GET(로드)
class BookList(generics.ListCreateAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#GET(로드)
class BookDetail(generics.RetrieveAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksDetailSerializer
    permission_classes = [permissions.IsAuthenticated]