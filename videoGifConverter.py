from moviepy.editor import VideoFileClip

#enter file name of video in quotation marks
clip = VideoFileClip("example.mp4")

#enter name for produced gif and fps
clip.write_gif("example.gif", fps = 10)