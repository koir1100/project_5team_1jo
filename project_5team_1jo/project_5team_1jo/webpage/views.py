from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import CustomUserCreationForm

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
def detail(request):
    context = {
        "title": "Detail Page",
        "result": 
            [
                {
                    "id": "4",
                    "title": "좋은 엄마 학교",
                    "author": "제서민 챈 지음; 정해영 옮김",
                    "keywords": ["가족", "학교", "친구"],
                    "recomNo": "20240401105251155100",
                },
                {
                    "id": "3",
                    "title": "출근하는 책들 : 읽는 삶은 일하는 삶을 어떻게 구하나",
                    "author": "지은이: 구채은",
                    "keywords": ["업무", "일터", "인간관계"],
                    "recomNo":"20240328103044369100",
                },
                {
                    "id": "2",
                    "title": "과학에서 인문학을 만나다 : 챗GPT의 시대 인문학에서 답을 찾다",
                    "author": "김유항,황진명 지음",
                    "keywords": ["인공지능", "챗GPT", "과학자"],
                    "recomNo":"20240328105133076100",
                },
                {
                    "id": "1",
                    "title": "수상한 단어들의 지도 : 꼬리에 꼬리를 무는 어원의 지적 여정",
                    "author": "데버라 워런 지음 ;홍한결 옮김",
                    "keywords": ["여행", "어원", "사연"],
                    "recomNo":"20240130133025518100",
                },
            ]
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
