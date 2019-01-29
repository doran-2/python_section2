from bs4 import BeautifulSoup
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html ="""
<html><body>
    <ul>
        <li><a id="naver" href="http://naver.com">naver</a></li>
        <li><a href="https://daum.com">daum</a></li>
        <li><a href="http://google.com">google</a></li>
        <li><a href="https://tistory.com">tistory</a></li>
    </ul>
<body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
test1 = soup.find_all('a',string="naver")
test2 = soup.find(id="naver")


li = soup.find_all(href=re.compile(r"^https://"))
print("li",li)

for e in li :
    print("string", e.string)
    print("attrs", e.attrs['href'])
