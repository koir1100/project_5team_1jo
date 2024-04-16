from django.urls import path

from . import views

app_name = 'webpage'

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("detail/", views.detail, name="detail"),
]