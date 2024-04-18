import requests
from bs4 import BeautifulSoup as BS
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db.settings')
django.setup()

from books_api import serializer
from books_api.serializer import RecomBooksSerializer

rest = requests.get("https://nl.go.kr/NL/search/openApi/saseoApi.do?key=d4e7415a231c75a620dd4615a4508a1902692938b60cb4c8b30eb6c8a07a3bc1&startRowNumApi=1&endRowNumApi=9999&start_date=20110315&end_date=20240415")

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

#print(len(data))
#print(data)
"""
for i in range(len(data)):
    serializer = RecomBooksSerializer(data=data[i])
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
"""
"""
sample = {
    'title': '80억 인류, 가보지 않은 미래 : 한중일 고령화, 서구의 극단주의, 신흥국의 인구폭발까지 세계정세의 대전환을 꿰뚫는 인구통계학의 통찰', 
    'author': '제니퍼 D. 스쿠바 지음 ;김병순 옮김', 
    'recomment': "초고령 사회로 인해 인구학에 대한 관심도 높아지고 있다. 이제 인구 80억이 넘는 세상이 도래한다고 하는데, 이러한 세상은 우리에게 기회의 보고일까? 아니면 전례 없는 문제의 장일까? 『80억 인류, 가보지 않은 미래』는 대전환기를 맞고 있는 세계 인구 변동의 흐름을 인구통계학의 관점으로 소개하고 있다. 이 책은 인구통계학자인 저자의 시각을 통해 전 세계의 인구 동향을 다루며, 다양한 인구 문제와 도전에 대한 해결책을 제시하고 있다. 또한 인구 증가와 감소가 현대 사회에 미치는 영향을 여러 가지 측면에서 탐구하고 있으며, 사회적 변화와 자원 부족 문제 등 현대 사회의 중요한 이슈도 함께 다루고 있다. 특히, 다양한 나라의 통계와 사례를 보여주며 이구학에 대한 기초 지식 없이도 쉽게 읽을 수 있도록 구성하였다. 저자는 인구통계학을 '과거와 미래를 연결하는 창'이라고 말한다. 이 책은 인구통계를 통해 과거의 정치,  사회, 경제에서의 변화를 이해하고 보다 정확하고 성공적으로 미래를 내다보는 데 도움을 줄 것이다.  ", 
    'recomno': '20240401115529297100', 
    'drcode': '5',
    }
"""

"""
1. 임의 유저가 조작할 수 없도록 제한하기
2. 유저에 대한 설정에 북마크 여부를 둘 것인지
"""