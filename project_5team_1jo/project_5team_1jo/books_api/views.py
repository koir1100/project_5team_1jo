from books.models import RecomBooks
from books_api.serializer import RecomBooksListSerializer
from books_api.serializer import RecomBooksDetailSerializer
from rest_framework import generics, permissions
#from . import permissions as api_permissions

#GET(로드)
class BookList(generics.ListAPIView):
    queryset = RecomBooks.objects.all().order_by('pk')
    serializer_class = RecomBooksListSerializer
    permission_classes = [permissions.IsAuthenticated]

#GET(로드)
class BookDetail(generics.RetrieveAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksDetailSerializer
    permission_classes = [permissions.IsAuthenticated]