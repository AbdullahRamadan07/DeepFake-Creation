import subprocess
import tkinter
from tkinter import *
from tkVideoPlayer import TkinterVideo
from PIL import Image, ImageTk


gp = Tk()
gp.geometry('1000x600+200+50')
gp.resizable(False, False)
gp.title('InterActive Status')

bgImg = tkinter.PhotoImage(file='.\\pythonProject\\pics\\background.png')
bg = Label(gp, image=bgImg)
bg.place(
    width=1000,
    height=600
)

footer_img_old = Image.open('.\\pythonProject\\pics\\footer.png')
footer_img_resized = footer_img_old.resize((1000, 50))
footer_img = ImageTk.PhotoImage(footer_img_resized)

footer = Label(gp, image=footer_img)
footer.place(
    x=0,
    y=545,
    width=1000
)

Tut = Image.open('.\\pythonProject\\pics\\Picture1.png')
Tut_resized = Tut.resize((400, 400))
Tut_img = ImageTk.PhotoImage(Tut_resized)

Tut_label = Label(gp, image=Tut_img)
Tut_label.place(
    x=90,
    y=100,
    width=400,
    height=400
    
)

l = Label(text = "Welcome To Interactive Statues",width=40,height=1,font=("Helvetica", 32),background="#4a148c",foreground="white")
l.pack()


# upload image button
Create_videos = Button(
    text='Create Deep Fake Videos',
    font=18,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: buImgClicked(),
    relief="flat"
)
Create_videos.place(
    x=650,
    y=250,
    width=300,
    height=50
)
ManageDb = Button(
    text='Manage Database',
    font=18,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: buImgClicked(),
    relief="flat"
)
ManageDb.place(
    x=650,
    y=350,
    width=300,
    height=50
)

def buImgClicked():
    gp.destroy()
    subprocess.call(["python", "CreateScreen.py"])

gp.mainloop()