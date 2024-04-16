from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    book_list = RecomBooks.objects.order_by('-recomno')[:10]
    context = {'books': book_list}
    return render(request, 'books/index.html')
    #output = ', '.join(b.title for b in book_list)
    #return HttpResponse(output)

def detail(request, recombooks_id):
    book = RecomBooks.objects.get(pk = recombooks_id)
    #return HttpResponse