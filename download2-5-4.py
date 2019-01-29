from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <div id="main">
        <h1>강의목록</h1>
        <ul class="lecs">
            <li>JAVA 프로그래밍</li>
            <li>파이썬 기초 프로그래밍</li>
            <li>파이썬 머신러닝 프로그래밍</li>
            <li>안드로이드 블루트스 프로그래밍</li>
        </ul>
    </div>
<body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

#div 태그이고 id가 main인 태그의 하위 h1을 가져오는 명령
h1 = soup.select("div#main > h1")
print("h1:",h1)

for z in h1:
    print(z.string)


list_li = soup.select("div#main > ul.lecs > li")


for k in list_li:
    print(k.string)
