import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://blogfiles.naver.net/20151222_18/s4616_1450771994984gQcKL_PNG/python.png"
htmlURL = "http://google.com"

savePath1 = "c:/test1.png"   
savePath2 = "c:/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료")
