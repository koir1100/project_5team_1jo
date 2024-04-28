from django.urls import path
from .views import *

urlpatterns=[
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/specific/<code>', BookSpecific.as_view(), name='book-specific'),
    path('books/search/', KeywordSearch.as_view(), name='book-search-default'),
    path('books/search/<keyword>', KeywordSearch.as_view(), name='book-search'),
    path('books/search/specific/<code>/<keyword>', KeywordSearch.as_view(), name='book-search-specific'),
]