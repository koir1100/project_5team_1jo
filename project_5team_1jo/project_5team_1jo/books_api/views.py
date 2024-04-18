from books.models import RecomBooks
from books_api.serializer import RecomBooksListSerializer
from books_api.serializer import RecomBooksDetailSerializer
from rest_framework import generics, permissions
from rest_framework_datatables.pagination import DatatablesLimitOffsetPagination
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

class RecomBooksListPagination(DatatablesLimitOffsetPagination):
    default_limit = 10

class BookSpecific(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer
    
    def get_queryset(self): 
        drcode = self.kwargs['code']
        return RecomBooks.objects.filter(drcode=drcode)