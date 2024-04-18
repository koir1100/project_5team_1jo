import requests
import sqlite3
import re
from bs4 import BeautifulSoup
from datetime import datetime
from konlpy.tag import Hannanum
from collections import Counter

key = "b4f9749d8859ee4e5584a3ecae413c4400466b92c3bf48c71f19b390eae80663"
startNum = 1
endNum = 10000
startDate = 20000101
endDate = int(datetime.today().strftime("%Y%m%d"))

res = requests.get("https://nl.go.kr/NL/search/openApi/saseoApi.do?key=%s&startRowNumApi=%d&endRowNumApi=%d&start_date=%d&end_date=%d" % (key, startNum, endNum, startDate, endDate))
soup = BeautifulSoup(res.text, "lxml")
hannanum = Hannanum()

input_list = [[] for i in range(int(soup.totalcount.text))]

for i, v in enumerate(soup.find_all("item")):
    input_list[i].append(v.recomtitle.text)
    input_list[i].append(v.recomauthor.text)

    recomment = BeautifulSoup(v.recomcontens.text, "html.parser").text.replace("\xa0", " ").replace("\n", "").replace("\r", "")
    retitle = re.sub(r"[^ㄱ-ㅣ가-힣0-9a-zA-Z\s]", "", v.recomtitle.text)
    reconten = re.sub(r"[^ㄱ-ㅣ가-힣0-9a-zA-Z\s]", "", recomment)
    nouns = hannanum.nouns(retitle) + hannanum.nouns(reconten)
    sorted_nouns = []
    
    input_list[i].append(recomment)
    input_list[i].append(v.recomno.text)
    input_list[i].append(int(v.drcode.text))

    for k in Counter(nouns).most_common():
        sorted_nouns.append(k[0])

    input_list[i].append(str(sorted_nouns))
    input_list[i] = tuple(input_list[i])

input_list = tuple(input_list)

conn = sqlite3.connect("./db.sqlite3")
cur = conn.cursor()

cur.execute("DELETE FROM books_recombooks")
cur.executemany("INSERT INTO books_recombooks (title, author, recomment, recomno, drcode, keyword) VALUES (?, ?, ?, ?, ?, ?)", input_list)
conn.commit()

cur.execute("SELECT COUNT(*) FROM books_recombooks")
check = cur.fetchall()

if check[0][0] == int(soup.totalcount.text):
    print(f"{check[0][0]} success!")
else:
    print(f"Fail: {check[0][0]} is not {int(soup.totalcount.text)}")

cur.close()
conn.close()