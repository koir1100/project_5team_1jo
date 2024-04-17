from django.urls import path
from .views import *

urlpatterns=[
    path('books/', books_list, name='question-list'),
]