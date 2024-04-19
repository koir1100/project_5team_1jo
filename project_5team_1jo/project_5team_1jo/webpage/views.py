from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from books.models import RecomBooks
from .forms import CustomUserCreationForm

import textwrap
from itertools import chain
from books.models import RecomBooks

import json

from .counter import *
import io
import urllib, base64

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
def list(request, drcode=0):
    context = {
        "title": "Book List",
        "drcode": drcode,
        "keyword": None,
    }

    return render(request, 'webpage/list.html', context)

@login_required(login_url='/webpage/signin')
def list_search(request, drcode=0, keyword=None):
    keyword_form = request.GET.get('keyword', None)
    keyword = keyword if keyword_form is None else keyword_form

    context = {
        "title": "Book List",
        "drcode": drcode,
        "keyword": keyword,
    }

    return render(request, 'webpage/list.html', context)

@login_required(login_url='/webpage/signin')
def detail(request, id=1):
    # session_id = request.session._get_or_create_session_key()
    # csrf_token = csrf.get_token(request)

    # headers = f"{{\"Cookie\":\"sessionid={session_id};csrftoken={csrf_token}\",\"X-CSRFToken\":\"{csrf_token}\"}}"
    # headers = json.loads(headers)

    # result = ""
    # result = requests.get('http://127.0.0.1:8000/rest/books/{}/'.format(id), headers=headers).json()
    result = RecomBooks.objects.get(pk=id)
    wrapper = textwrap.TextWrapper(width=2000, replace_whitespace=False)
    temp = result.recomment
    
    contents = [wrapper.wrap(i) for i in temp.split('<br/>') if i != '']
    contents = chain.from_iterable(contents)

    context = {
        "title": result.title,
        "author": result.author,
        "recomment": contents,
        "recomno": result.recomno,
        "keyword": json.loads(result.keyword)[:3],
    }

    return render(request, 'webpage/detail.html', context)

@login_required(login_url='/webpage/signin')
def keyword(request, drcode=0):
    if drcode == 0:
        books = RecomBooks.objects.all()
    else:
        books = RecomBooks.objects.filter(drcode=drcode)

    keywords = makeCounter(books)
    commons = makeCommon(keywords)
    icon = Image.open('activity.png')
    img = Image.new('RGB', icon.size, (255, 255, 255))
    img.paste(icon, icon)
    img = np.array(img)

    wordcloud = WordCloud(font_path="tree.ttf", background_color="white", mask=img, colormap='inferno')
    wc = wordcloud.generate_from_frequencies(keywords)

    plt.figure(figsize=(6.5,5))
    plt.axis('off')
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
    plt.imshow(wc)

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    context = {
        'image': uri,
        'keyword': commons,
        'drcode': drcode
    }

    return render(request, 'webpage/keyword.html', context)

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

