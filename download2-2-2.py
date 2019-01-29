import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://blogfiles.naver.net/20151222_18/s4616_1450771994984gQcKL_PNG/python.png"
htmlURL = "http://google.com"

savePath1 = "c:/test1.png"
savePath2 = "c:/index.html"

#예전 방식의 파일 저장
f = dw.urlopen(imgUrl).read()
saveFile1 = open(savePath1, 'wb') # W:Write , r:Read , a:Add
saveFile1.write(f)
saveFile1.close();

#바뀐 형식의 파일 저장
f2 = dw.urlopen(htmlURL).read()
with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료")
