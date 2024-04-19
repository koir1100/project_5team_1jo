from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'models', KeywordSearch, basename='RecomBooks')

urlpatterns=[
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetail.as_view(), name='book-detail'),
    path('search/', KeywordSearch.as_view({'get':'search'}), name='search'),
]

urlpatterns += router.urls