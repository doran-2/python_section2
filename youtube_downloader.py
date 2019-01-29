import pytube


yt = pytube.YouTube("https://www.youtube.com/watch?v=9HSU6iEJYqM")
videos = yt.streams.all()

print('videos',videos)

#for i in range(len(videos)) : #range(1,6) 1,2,3,4,5
#    print(i, ',', videos[i])
