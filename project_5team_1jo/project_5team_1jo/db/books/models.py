from django.db import models

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
"""
출력 결과 필드
NO  필드                값           설명
1	totalCount          Integer	    해당분류 총 개수
2	recom_no	        Integer	    추천번호
3	recom_code	        Integer	    분류번호
4	decode	            String	    분류명
5	recom_title	        String      추천도서 제목
6	recom_author	    String	    추천도서 작가
7	recom_publisher	    String	    추천도서 자료출판사
8	recom_callno	    String  	추천도서 청구기호
9	recom_file_path	    String  	추천도서 이미지 경로
10	recom_mokcha	    String  	추천도서 목차
11	recom_contents	    String  	추천도서 자료내용
12	recom_reg_dt	    String  	추천도서 등록일
13	control_no	        String  	추천도서 제어번호
14	publish_year	    Integer	    추천도서 발행년도
15	recom_year	        Integer 	추천도서 추천년도
16	recom_month	        Integer	    추천도서 추천월
17	mokchFilePath	    String  	목차 이미지 경로
18	recome_isbn	        String	    추천도서 ISBN
"""
"""
1. 장르별 키워드 빈도수 시각화 결과 *
2. 장르별 추천 도서 목록 및 하이퍼링크
3. 키워드 검색 *
4. 회원가입 / 로그인 기능

키워드 지정을 어떻게 할까?

"""

class RecomBooks(models.Model):
    recom_no = models.BigIntegerField(default=0, primary_key=True) #추천 번호
    decode = models.CharField(max_length=10) #분류명
    recom_title = models.CharField(max_length=200) #추천도서 제목
    recom_author = models.CharField(max_length=100) #도서 작가
    isbn = models.BigIntegerField(default=9700000000000) #ISBN
    #bookmark = models.BooleanField(default=False) #북마크 여부

    def __str__(self):
        return f'{self.recom_title}'


class BookDetalis(models.Model):
    title = models.ForeignKey(RecomBooks, on_delete = models.CASCADE)
    recom_contents = models.CharField(max_length=1000) #자료내용
    keyword = models.CharField(max_length=30) #키워드

    def __str__(self):
        return f'제목:{self.title} 키워드:{self.keyword}'