from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    book_list = RecomBooks.objects.order_by('-recom_no')[:10]
    output = ', '.join(b.recom_title for b in book_list)
    return HttpResponse(output)
