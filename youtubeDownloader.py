from pytubefix import YouTube
from pytubefix.cli import on_progress
 
#replace url with youtube video link between quotation marks
url = "url here"
 
yt = YouTube(url, on_progress_callback = on_progress)
print("Title: ", yt.title)
print("Views: ", yt.views)
 
ys = yt.streams.get_highest_resolution()

#enter desired file path in quotation marks
#set mp3 to True if you want to download video as mp3
#otherwise set it to False
ys.download(r"file path here", mp3=True)