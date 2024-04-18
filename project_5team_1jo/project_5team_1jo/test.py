import requests
from bs4 import BeautifulSoup as BS
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_5team_1jo.settings')
django.setup()

from api_data2db import data2db

rest = requests.get("https://nl.go.kr/NL/search/openApi/saseoApi.do?key=d4e7415a231c75a620dd4615a4508a1902692938b60cb4c8b30eb6c8a07a3bc1&startRowNumApi=1&endRowNumApi=9999&start_date=20090101&end_date=20241231")

"""
요청 변수(request parameter)
NO  요청변수        형식                설명
1	key	            String(필수)    발급키
2	startRowNumApi	integer         시작번호(1부터시작)
3	endRowNemApi	integer	        종료번호
4	start_date	    integer	        검색시작일
5	end_date	    integer	        검색종료일
6	drCode	        integer	        분류번호(11:문학, 6:인문과학, 5:사회과학, 4:자연과학)
"""

soup = BS(rest.text, 'html.parser')

bookname = soup.find_all("recomtitle")
authors = soup.find_all("recomauthor")
contents = soup.find_all("recomcontens")
recom_no = soup.find_all("recomno")
drcode = soup.find_all("drcode")
pub = soup.find_all("recompublisher")

data = []

for i in range(len(bookname)):
    contentsoup = BS(contents[i].text).text

    contentsoup = contentsoup.replace("\xa0", " ")
    contentsoup = contentsoup.replace("\n", " ")
    #print(len(contentsoup))
    data_dict = {
        "id":i,
        "title":bookname[i].text,
        "author":authors[i].text,
        "recomment":contentsoup,
        "recomno":recom_no[i].text,
        "drcode":drcode[i].text
    }
    data.append(data_dict)

data2db(data)

"""
1. 임의 유저가 조작할 수 없도록 제한하기
2. 유저에 대한 설정에 북마크 여부를 둘 것인지
"""
