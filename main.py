import pytube

#ask for the link from user
#https://www.youtube.com/watch?v=dQw4w9WgXcQ


link = input("Enter the link of YouTube video you want to download:  ")
try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = pytube.YouTube(link)
except:
    print("Connection Error")

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

stream = yt.streams.get_highest_resolution()


try:
    # downloading the video
    stream.download()
except:
    print("Some Error!")
print('Task Completed!')
