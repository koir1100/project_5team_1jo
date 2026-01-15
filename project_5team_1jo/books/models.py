from django.db import models

"""
출력 결과 필드
NO  필드                값           설명
1	totalcount          Integer	    해당분류 총 개수 -
2	recomno	            Integer	    추천번호 *
3	drcode	            Integer	    분류번호 *
4	drcodename	        String	    분류명 -
5	recomtitle	        String      추천도서 제목 *
6	recomauthor	        String	    추천도서 작가 *
7	recompublisher	    String	    추천도서 자료출판사 -
8	recomcallno	        String  	추천도서 청구기호 -
9	recom_file_path	    String  	추천도서 이미지 경로 -
10	recommokcha	        String  	추천도서 목차 -
11	recomcontens	    String  	추천도서 자료내용 *
12	regdate	            String  	추천도서 등록일 -
13	controlno	        String  	추천도서 제어번호 -
14	publishyear	        Integer	    추천도서 발행년도 -
15	recomyear	        Integer 	추천도서 추천년도 -
16	recommonth	        Integer	    추천도서 추천월 -
17	mokchfilepath	    String  	목차 이미지 경로 -
18	recomisbn	        String	    추천도서 ISBN -
"""

class RecomBooks(models.Model):
    title = models.CharField(max_length=200) #추천도서 제목
    author = models.CharField(max_length=100) #도서 작가
    recomment = models.CharField(max_length=2000, default="없음") #자료내용(코멘트)
    recomno = models.CharField(max_length=20, default="0000") #20자리의 번호 코드는 IntegerField의 범위를 넘음, 문자열 형태로 받아야 함
    drcode = models.IntegerField(default=0) #분류 번호
    keyword = models.JSONField(max_length=2000, default=list) #별도로 추출한 키워드 | ",".join()
    #bookmark = models.BooleanField(default=False) #북마크 여부

    def __str__(self):
        return f'제목:{self.title}, 작가:{self.author}'
