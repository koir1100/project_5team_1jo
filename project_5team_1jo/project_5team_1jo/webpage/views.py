from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "Book Recommendation",
    }

    return render(request, 'webpage/index.html', context)
    # return HttpResponse("Hello world, I am in the index.")

def home(request):
    context = {
        "title": "Home Page",
    }

    return render(request, 'webpage/home.html', context)

def search(request):
    context = {
        "title": "Search Page",
    }

    return render(request, 'webpage/search.html', context)
