from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:book_recomno>/', views.detail, name='detail'),
]
