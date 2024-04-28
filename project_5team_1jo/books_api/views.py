from books.models import RecomBooks
from rest_framework import generics, permissions
from books_api.serializer import RecomBooksListSerializer, RecomBooksDetailSerializer
from rest_framework_datatables.pagination import DatatablesLimitOffsetPagination
from django.db.models import Q

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

class KeywordSearch(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomBooksListPagination
    serializer_class = RecomBooksListSerializer

    def get_queryset(self):
        try:
            drcode = self.kwargs.get('code', 0)
            keyword = self.kwargs['keyword']

            if drcode != 0:
                return RecomBooks.objects.filter(drcode=drcode).filter(Q(keyword__0__icontains=keyword)|Q(keyword__1__icontains=keyword)|Q(keyword__2__icontains=keyword))
            else:
                return RecomBooks.objects.filter(Q(keyword__0__icontains=keyword)|Q(keyword__1__icontains=keyword)|Q(keyword__2__icontains=keyword))
        except KeyError:
            return RecomBooks.objects.none()
    