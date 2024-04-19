from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

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