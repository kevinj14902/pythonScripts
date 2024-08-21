from moviepy.editor import VideoFileClip

clip = VideoFileClip("video.mp4")
clip.write_gif("newgif.gif", fps = 10)