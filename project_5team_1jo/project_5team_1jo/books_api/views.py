from books.models import RecomBooks
from rest_framework import generics, permissions
from books_api.serializer import RecomBooksListSerializer, RecomBooksDetailSerializer
from rest_framework_datatables.pagination import DatatablesLimitOffsetPagination

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


class KeywordSearch(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer
    #queryset = RecomBooks.objects.all()

    def get_queryset(self):
        keyword = self.kwargs['keyword']
        #return RecomBooks.objects.filter(keyword=keyword)
        return RecomBooks.objects.filter(keyword__contains=keyword)
    



class BookSpecific(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer
    
    def get_queryset(self): 
        drcode = self.kwargs['code']
        return RecomBooks.objects.filter(drcode=drcode)
