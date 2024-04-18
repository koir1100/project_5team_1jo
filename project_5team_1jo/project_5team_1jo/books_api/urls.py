from django.urls import path
from .views import *

urlpatterns=[
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail')
]