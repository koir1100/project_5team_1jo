from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from books_api.serializer import RecomBooksListSerializer, RecomBooksDetailSerializer
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
    serializer_class = RecomBooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class KeywordSearch(viewsets.ViewSet):
    queryset = RecomBooks.objects.all()
    serializer_class = RecomBooksSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def search(self, request):
        search_term = request.query_params.get('search_term', '')
        queryset = self.queryset.filter(data_field__icontains=search_term)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class RecomBooksListPagination(DatatablesLimitOffsetPagination):
    default_limit = 10

class BookSpecific(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer
    
    def get_queryset(self): 
        drcode = self.kwargs['code']
        return RecomBooks.objects.filter(drcode=drcode)
