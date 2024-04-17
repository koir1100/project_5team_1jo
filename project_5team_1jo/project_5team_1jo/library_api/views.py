from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import xmltodict
import json
import requests
import re

# Create your views here.
PAGE_RANGE = 5
PAGE_SIZE = 10

def paginate(max_count, page_size, page_number):
    start_index = page_number * page_size
    end_index = start_index + page_size

    if max_count > end_index:
        end_index = max_count

    return start_index, end_index

def get_origin_data(start=1, end=1):
    origin_xml = requests.get("https://nl.go.kr/NL/search/openApi/saseoApi.do?key=c3ce87dbac545d27063e13da0cd917b9b2f314855cb43e85b72d77d1474ff070&startRowNumApi={}&endRowNumApi={}&start_date=20240101&end_date=20240331".format(start, end))

    # 출처: https://stackoverflow.com/a/59895826
    decode_xml = origin_xml.content.decode("utf-8")
    parsed_data = xmltodict.parse(decode_xml)

    # 출처: https://hayjo.tistory.com/75
    json_data = json.dumps(parsed_data, ensure_ascii=False)

    cleansing_data = cleanhtml(json_data)

    # 출처: https://www.jungyin.com/123
    real_json_data = json.loads(cleansing_data)

    return real_json_data

# 출처: https://stackoverflow.com/a/12982689
def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>')
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def convert_int(s):
    try:
        i = int(s)
    except ValueError:
        i = 1
    
    if i < 1 or i > 50:
        i = 1
    return i

@api_view()
def list_books(request, page):
    cur_page = convert_int(page)

    json_data = get_origin_data()
    max_count = json_data['channel']['totalCount']

    start_idx, end_idx = paginate(int(max_count), PAGE_SIZE, cur_page)
    real_json_data = get_origin_data(start_idx, end_idx)
    max_count = real_json_data['channel']['totalCount']

    filter_data = real_json_data['channel']['list']
    new_data = list()
    attri_list = ['drCode', 'recomNo', 'recomcontens', 'recomauthor', 'recomtitle']

    if type(filter_data) is dict:
        values = list(filter_data.values())[0]
        temp = dict()
        for key in values.keys():
            if key in attri_list:
                temp[key] = values.get(key)
        new_data.append(temp)
    else:
        for record in filter_data:
            values = dict()
            for key in record['item'].keys():
                if key in attri_list:
                    values[key] = record['item'][key]
            new_data.append(values)

    return Response(new_data)

@api_view
def detail(request):
    return Response()