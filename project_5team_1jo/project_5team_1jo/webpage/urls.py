from django.urls import path

from . import views

app_name = 'webpage'

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("list/", views.list, name="list-all"),
    path("list/<int:drcode>", views.list, name="list-specific"),
    path("list/search/", views.list_search, name="list-keyword-default"),
    path("list/search/<str:keyword>", views.list_search, name="list-keyword"),
    path("detail/<int:id>", views.detail, name="detail"),
    path('signin/', views.login_user, name='signin'),
    path('signout/', views.logout_user, name='signout'),
    path('register/', views.register_user, name='register'),
    path('keyword/', views.keyword, name="keyword-all"),
    path('keyword/<int:drcode>/', views.keyword, name="keyword-specific"),
]