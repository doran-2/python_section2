from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html ="""
<html><body>
    <ul>
        <li><a href="http://naver.com">naver</a></li>
        <li><a href="http://daum.com">daum</a></li>
        <li><a href="http://google.com">google</a></li>
        <li><a href="http://tistory.com">tistory</a></li>
    </ul>
<body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
#print('links:', tyoe(links)
a = soup.find_all("a", string="daum")
b = soup.find_all("a", limit=3)
c = soup.find_all(string=["naver", "google"])

for a in links:
    #print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print('txt :', txt, 'href: ', href)
