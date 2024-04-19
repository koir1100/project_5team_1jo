from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from books_api.serializer import RecomBooksListSerializer, RecomBooksDetailSerializer
from rest_framework_datatables.pagination import DatatablesLimitOffsetPagination
from rest_framework.decorators import api_view

#GET(로드)
class BookList(generics.ListAPIView):
    queryset = RecomBooks.objects.all().order_by('pk')
    serializer_class = RecomBooksListSerializer
    permission_classes = [permissions.IsAuthenticated]

#GET(로드)
class BookDetail(generics.RetrieveAPIView):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecomBooksListPagination(DatatablesLimitOffsetPagination):
    default_limit = 10


class KeywordSearch(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer
    #queryset = RecomBooks.objects.all()

    """def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)"""

    """def search(self, request):
        keyword = self.kwargs['keyword']
        return RecomBooks.objects.filter(keyword=keyword)
    """
    def get_queryset(self):
        keyword = self.kwargs['keyword']
        #return RecomBooks.objects.filter(keyword=keyword)
        return RecomBooks.objects.filter(keyword__contains=keyword)
    
    """
        search_term = request.query_params.get('keyword', None)
        queryset = self.queryset.filter(keyword__contains=search_term)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        """



class BookSpecific(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer
    
    def get_queryset(self): 
        drcode = self.kwargs['code']
        return RecomBooks.objects.filter(drcode=drcode)
