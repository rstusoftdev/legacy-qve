# R Studio Editing Software (RSES) by R Studio Coding section
# ©2021 R Stu Team | All Right Reserved


#Packages
# pip install moviepy
# pip install tk
# pip install alive-progress

#Import

from alive_progress import alive_bar; import time, logging
from time import sleep
import itertools
import threading
import sys,time,os
from tkinter import *
from moviepy.editor import *

#Loading Terminal: R Stu Team Console System

text = "\nmake sure you have the video named [1.mp4] and [2.mp4] or the audio named [audio.mp3]!                                            "
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

typewriter(text)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('R Stu Team Console System')

with alive_bar(1000) as bar:
    for i in range(1000):
        if i in (254, 254):
            logger.info('running package')
        if i in (454, 454):
            logger.info('read the package')
        if i in (690, 690):
            logger.info('detecting.....')
        if i in (795, 795):
            logger.info('running package')
        if i in (843, 843):
            logger.info('opening the software')
        if i in (950, 950):
            logger.info('almost done....')
        time.sleep(0.01)
        bar()


done = False
 
def animate():
    for c in itertools.cycle(['|', '/', '-', '']):
        if done:
            break
        sys.stdout.write('\rRunning the code ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rLaunched!            ')
 
loadingd = threading.Thread(target=animate)
loadingd.start()



#Variable

clip1 =VideoFileClip("1.mp4")
clip2 =VideoFileClip("2.mp4")


#Functions

def mix():
    final_clip = concatenate_videoclips([clip1,clip2])
    final_clip.write_videofile("Untitled Mix Video.mp4")

def mirror():
    clip_mirror = clip1.fx(vfx.mirror_x)
    clip_mirror.write_videofile("Untitled Mirror Video.mp4")

def resize():
    r=float(input("Enter your Size :"))
    clip_resize=clip1.resize(r)
    clip_resize.write_videofile("Untitled Resize Video.mp4")

def Effects_speed():
    speed =float(input("Enter your Speed :"))
    clip_speed= clip1.fx(vfx.speedx, speed)
    clip_speed.write_videofile("Untitled Speed Video.mp4")

def Effects_colour():
    colour=float(input("Value of Darkness :"))
    clip_color=clip1.fx(vfx.colorx , colour)
    clip_color.write_videofile("Untitled Colour Video.mp4")

def trim():
    starting=int(input("Enter Starting Point Here :"))
    ending=int(input("Enter Starting Point Here :"))
    clip_trim = clip1.cutout(starting,ending)
    clip_trim.write_videofile("Untitled Trim Video.mp4")

def audio_file():
    import moviepy.editor as mpe
    audioclip=mpe.AudioFileClip("audio.mp3")
    videoclip=mpe.videoclip.set_audio(audioclip)
    final_clip=videoclip.set_audio(audioclip)
    final_clip.write_videofile("Untitled Audio.mp4")


#Main Screen
#UI

root = Tk()

border_color = Frame(root, background="#232323")
var = StringVar()
label = Label( root, bg="#232323", fg="white",textvariable=var )

root.iconbitmap("favicon.ico")
root.title("RS Editing Software V0.1.210621 beta indev dev (unstable)")
root.geometry("910x200")
root.resizable(0, 0)
root.config(bg="#232323")


#Button UI
#Mix

b=Button(root,text="Mix",relief=GROOVE,bg="#232323",fg="white",command=mix)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Mirror

b=Button(root,text="Mirror",relief=GROOVE,bg="#232323",fg="white",command=mirror)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Resize

b=Button(root,text="Resize",relief=GROOVE,bg="#232323",fg="white",command=resize)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Speed

b=Button(root,text="Speed",relief=GROOVE,bg="#232323",fg="white",command=Effects_speed)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Colour

b=Button(root,text="Colour",relief=GROOVE,bg="#232323",fg="white",command=Effects_colour)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Trim

b=Button(root,text="Trim",relief=GROOVE,bg="#232323",fg="white",command=trim)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Audio

b=Button(root,text="Audio",relief=GROOVE,bg="#232323",fg="white",command=audio_file)
b.pack(side="left",padx=20)
b.config(width=8,height=3)

#Text Copyright

var.set("©2021 R Stu Team")
label.place(relx = 0.5,rely = 1,anchor = 's')

#Launch Software

done = True
root.mainloop()
