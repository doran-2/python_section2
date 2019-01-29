import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://ssl.pstatic.net/tveta/libs/1215/1215876/f3f4ebcf52539bc2a6c4_20190121175120928.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1224/1224374/57e768280e9d14b792f1_20190117121826220.mp4-pBASE-v0-f72259-20190117122020853.mp4"

savePath1 = "c:/homework.jpg"
savePath2 = "c:/homework.mp4"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(videoUrl, savePath2)

print("다운로드 완료")
