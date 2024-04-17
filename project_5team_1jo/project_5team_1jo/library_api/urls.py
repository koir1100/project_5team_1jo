from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('list/<int:page>/', views.list_books, name='list-books'),
    path('detail/<int:recomid>/', views.detail, name='detail'),
]