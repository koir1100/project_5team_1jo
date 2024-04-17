from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('list/<int:page>/', views.list_books, name='list-books'),
    path('list/<str:type>/<int:page>/', views.list_books, name='list-books-type'),
    path('detail/<int:recomid>/', views.detail_book, name='detail-book'),
]