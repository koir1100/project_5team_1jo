from django.urls import path

from . import views

app_name = 'webpage'

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("detail/", views.detail, name="detail"),
    path('signin/', views.login_user, name='signin'),
    path('signout/', views.logout_user, name='signout'),
    path('register/', views.register_user, name='register'),
]