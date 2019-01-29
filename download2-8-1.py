from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="
quote = rep.quote_plus("파이썬")

url = base + quote

savePath = "C:\\python_work\\image_down\\"

res = req.urlopen(url).read()

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")

#print(img_list)

for i, element in enumerate(img_list,1):
    #print(i,':',element['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    #print(fullFileName)
    req.urlretrieve(element['data-source'], fullFileName)

print("다운로드완료")
