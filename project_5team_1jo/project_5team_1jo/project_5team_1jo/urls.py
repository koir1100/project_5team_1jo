"""
URL configuration for project_5team_1jo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# https://stackoverflow.com/a/55111389
from django.views.debug import default_urlconf
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', default_urlconf),
    path('admin/', admin.site.urls),
    path('scrap/', include('scrap.urls')),
    path('books/', include('books.urls')),
    path('rest/', include('books_api.urls')),
    path('webpage/', include("webpage.urls")),
    path('api/', include("library_api.urls")),
]
