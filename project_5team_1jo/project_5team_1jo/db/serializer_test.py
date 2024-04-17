from books.models import RecomBooks
from books_api.serializer import RecomBooksSerializer
from rest_framework.renderers import JSONRenderer
import json

sample = {
    'id': 7, 
    'title': '80억 인류, 가보지 않은 미래 : 한중일 고령화, 서구의 극단주의, 신흥국의 인구폭발까지 세계정세의 대전환을 꿰뚫는 인구통계학의 통찰', 
    'author': '제니퍼 D. 스쿠바 지음 ;김병순 옮김', 
    'recomment': "초고령 사회로 인해 인구학에 대한 관심도 높아지고 있다. 이제 인구 80억이 넘는 세상이 도래한다고 하는데, 이러한 세상은 우리에게 기회의 보고일까? 아니면 전례 없는 문제의 장일까? 『80억 인류, 가보지 않은 미래』는 대전환기를 맞고 있는 세계 인구 변동의 흐름을 인구통계학의 관점으로 소개하고 있다. 이 책은 인구통계학자인 저자의 시각을 통해 전 세계의 인구 동향을 다루며, 다양한 인구 문제와 도전에 대한 해결책을 제시하고 있다. 또한 인구 증가와 감소가 현대 사회에 미치는 영향을 여러 가지 측면에서 탐구하고 있으며, 사회적 변화와 자원 부족 문제 등 현대 사회의 중요한 이슈도 함께 다루고 있다. 특히, 다양한 나라의 통계와 사례를 보여주며 이구학에 대한 기초 지식 없이도 쉽게 읽을 수 있도록 구성하였다. 저자는 인구통계학을 '과거와 미래를 연결하는 창'이라고 말한다. 이 책은 인구통계를 통해 과거의 정치,  사회, 경제에서의 변화를 이해하고 보다 정확하고 성공적으로 미래를 내다보는 데 도움을 줄 것이다.  ", 
    'recomno': '20240401115529297100', 
    'drcode': '5',
    'publisher':""
    }

serializer= RecomBooksSerializer(sample)
print(serializer.data)
json_str = JSONRenderer().render(serializer.data)
print(json_str)

data = json.loads(json_str)
serializer = RecomBooksSerializer(data=data)
print(serializer.is_valid())

new_data = serializer.save()