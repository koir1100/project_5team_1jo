from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def index(request):
    key = "b4f9749d8859ee4e5584a3ecae413c4400466b92c3bf48c71f19b390eae80663"
    startNum = 1
    endNum = 1
    startDate = 20200101
    endDate = 20200110
    drcode = 11
    res = requests.get("https://nl.go.kr/NL/search/openApi/saseoApi.do?key=%s&startRowNumApi=%d&endRowNumApi=%d&start_date=%d&end_date=%d&drcode=%d" % (key, startNum, endNum, startDate, endDate, drcode))
    soup = BeautifulSoup(res.text, "lxml")
    return render(request, 'scrap/index.html')