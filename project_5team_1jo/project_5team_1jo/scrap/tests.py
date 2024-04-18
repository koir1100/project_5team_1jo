import requests
from bs4 import BeautifulSoup
import re

key = "b4f9749d8859ee4e5584a3ecae413c4400466b92c3bf48c71f19b390eae80663"
startNum = 1
endNum = 10
startDate = 20200101
endDate = 20200131
drcode = 11
res = requests.get("https://nl.go.kr/NL/search/openApi/saseoApi.do?key=%s&startRowNumApi=%d&endRowNumApi=%d&start_date=%d&end_date=%d" % (key, startNum, endNum, startDate, endDate))
soup = BeautifulSoup(res.text, "lxml")
print(soup.find("totalcount").text)
for item in soup.find_all("item"):
    print("추천번호 : ",item.recomno.text)
    print("dr코드 : ",item.drcode.text)
    print("제목 : ",item.recomtitle.text)
    print("작가 : ",item.recomauthor.text)
    recomConten = item.recomcontens.text
    pattern = re.compile("<.*?>")
    recomConten = re.sub(pattern, "", recomConten)
    pattern = re.compile(r'&nbsp;')
    recomConten = re.sub(pattern, "", recomConten)
    print(recomConten)

