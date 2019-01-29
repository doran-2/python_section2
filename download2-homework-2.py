from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net//"

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

#print(soup)
#다음 실시간 검색어 인기순위 25위를 가져오는 예제

realtimeTop10 = soup.select("div.rank_cont[aria-hidden='true'] > span.txt_issue > a")
#ol.list_hotissue issue_row
#print(realtimeTop10)
#print(type(realtimeTop10))

for i, element in enumerate(realtimeTop10,1):
    print(i,'.',element.string,' --> ', element.get('href'))
