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
from books.models import RecomBooks

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
def detail(request, id=6):
    wrapper = textwrap.TextWrapper(width=600, replace_whitespace=False)
    temp = """‘인간이 상상하지 못한 혁신과 발전을 이끌어 낼 수 있는 도구’

이 책은 인공지능에 관한 기술적 설명보다는 인공지능이 의료, 금융 등 다양한 산업 분야에서 어떤 역할을 하게 되는지 또 인공지능으로 인해 사라질 직업과 새로이 나타날 직업 등 인공지능이 미래에 우리 삶에 끼칠 영향들을 다루고 있다. 그리고 급변하는 시대에 대한민국 및 세계 각국에서는 인공지능에 어떻게 대비하고 있는지 비전문가도 쉽게 이해할 수 있게 내용을 풀어 설명하고 있다.

하지만 인공지능 기술을 터득하고 체화하는 데 걸리는 시간보다 인공지능 기술이 발전하는 속도가 너무 빠르다 보니 인공지능을 잘 활용하지 못하고 인공지능에 두려움을 갖는 사람들이 있는 것도 사실이다. 이 책을 읽고 마음속에 있던 벽을 허물어 인공지능에 한 걸음 더 가까이 다가가 보는 건 어떨까? 변화하는 시대에 같이 발맞추어 가기 위해서 말이다."""
    
    contents = [wrapper.wrap(i) for i in temp.split('\n') if i != '']
    contents = chain.from_iterable(contents)

    context = {
        "title": "2024 AI 트렌드 : 한발 더 빠르게, 누구보다 깊이 있게 AI로 송두리째 바뀔 세상을 포착하다",
        "author": "딥앤와이랩스,류성일,이규남,황동건,이영표,조현서,박준상,홍준의 지음",
        "recomment": contents,
        "recomno": "20240130152736808100",
        "keyword": "인공지능, 변화, 기술",
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

