from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import CustomUserCreationForm
import requests

import textwrap
from itertools import chain

import json
from django.middleware import csrf

# Create your views here.

@login_required(login_url='/webpage/signin')
def index(request):
    context = {
        "title": "Book Recommendation",
    }

    return render(request, 'webpage/index.html', context)
    # return HttpResponse("Hello world, I am in the index.")

@login_required(login_url='/webpage/signin')
def home(request):
    context = {
        "title": "Home Page",
    }

    return render(request, 'webpage/home.html', context)

@login_required(login_url='/webpage/signin')
def list(request, page=1, type=None):
    result = ""
    if type is not None:
        result = requests.get('http://127.0.0.1:8000/api/list/{}/{}'.format(type, page)).json()
    else:
        result = requests.get('http://127.0.0.1:8000/api/list/{}'.format(page)).json()
    
    category = ""
    if type == "li":
        category = "문학 분야"
    elif type == "hs":
        category = "인문과학 분야"
    elif type == "ss":
        category = "사회과학 분야"
    elif type == "ns":
        category = "자연과학 분야"
    else:
        category = "전 분야"

    context = {
        "title": "Book List",
        "category": category,
        "result": result,
        "page": page,
    }

    return render(request, 'webpage/list.html', context)

@login_required(login_url='/webpage/signin')
def detail(request, id=1):
    session_id = request.session._get_or_create_session_key()
    csrf_token = csrf.get_token(request)

    headers = f"{{\"Cookie\":\"sessionid={session_id};csrftoken={csrf_token}\",\"X-CSRFToken\":\"{csrf_token}\"}}"
    headers = json.loads(headers)

    result = ""
    result = requests.get('http://127.0.0.1:8000/rest/books/{}/'.format(id), headers=headers).json()

    wrapper = textwrap.TextWrapper(width=600, replace_whitespace=False)
    temp = result['recomment']
    
    contents = [wrapper.wrap(i) for i in temp.split('\n') if i != '']
    contents = chain.from_iterable(contents)

    context = {
        "title": result['title'],
        "author": result['author'],
        "recomment": contents,
        "recomno": result['recomno'],
        "keyword": json.loads(result['keyword'].replace("'","\""))[:4],
    }

    return render(request, 'webpage/detail.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/webpage')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Not exist your user info')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Login Success')
            login(request, user)
            return redirect('/webpage')
        else:
            messages.error(request, 'Incorrect user info')
            return redirect('/webpage/signin')
    
    return render(request, 'webpage/signin.html', {'title': 'Sign in Page'})

def register_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Signup Success')
            login(request, user)
            return redirect('/webpage')
        else:
            messages.error(request, 'Something is wrong...')
    
    context = {
        "form": form,
        'title': 'Sign up Page',
    }

    return render(request, 'webpage/register.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('/webpage')
