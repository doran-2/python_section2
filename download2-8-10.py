from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")

url = base + quote

savePath = "C:\\python_work\\image_down_2\\"

res = req.urlopen(url).read()

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("ul.slides")[0]

#print(img_list)

for i, element in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(element.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    #print(fullFileName)
    req.urlretrieve(element.select_one("div.block_media > a > img")['src'], fullFileName)

print("다운로드완료")
