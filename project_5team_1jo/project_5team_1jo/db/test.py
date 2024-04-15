import requests
from bs4 import BeautifulSoup as BS

rest = requests.get("https://www.nl.go.kr/NL/search/openApi/search.do?key=&kwd=%ED%86%A0%EC%A7%80")
soup = BS(rest.text, 'html.parser')

print(soup.prettify())