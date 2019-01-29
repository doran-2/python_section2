from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://m.apt2you.com/apt/saleHouse/selectHouseName.do"
res = req.urlopen(url).read().decode('euc-kr')
soup = BeautifulSoup(res, "html.parser")

#print(soup)
#아파트투유의 분양정보를 가져오는 예제

#installment_sale = soup.select("div.tb_1 > table > tbody")
installment_sale = soup.select("div.tb_1 > table > tbody > tr > td")

#print(installment_sale)
#print(type(installment_sale))

i=0;
for j,element in enumerate(installment_sale,i):
    if j > 2:
        name = element.select("a")

        if len(name)==1:
            i= i+1;
            print(i,'.',name[0].string.replace(' ','').strip(),' : ',end='')
        else:
            print(element.text.replace(' ','').strip())
