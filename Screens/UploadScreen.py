import subprocess
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
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

frame = Frame(gp, width=550, height=350)
frame.place(
    x=215,
    y=20
)

# back button
back_btn = Button(
    text='Back',
    font=20,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_btn_clicked(),
    relief="flat"
)
back_btn.place(
    x=10,
    y=20,
    width=120,
    height=40
)

# add button
add_btn = Button(
    text='ADD',
    font=20,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command= lambda: click_add_btn(),    
    relief="flat"
)
add_btn.place(
    x=225,
    y=415,
    width=120,
    height=40
)

# delete button
delete_btn = Button(
    text='DELETE',
    font=20,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command= lambda: click_del_btn(),
    relief="flat"
)
delete_btn.place(
    x=615,
    y=415,
    width=120,
    height=40
)

# play button
play_img_old = Image.open('.\\pythonProject\\pics\\play.jpg')
play_img_resized = play_img_old.resize((55, 65))
play_img = ImageTk.PhotoImage(play_img_resized)
play_btn = Button(
    image=play_img,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playVideo(),
    relief="flat"
)
play_btn.place(
    x=375,
    y=420,
    width=50,
    height=30
)

# pause button
pause_img_old = Image.open('.\\pythonProject\\pics\\pause.jpg')
pause_img_resized = pause_img_old.resize((55, 65))
pause_img = ImageTk.PhotoImage(pause_img_resized)
pause_btn = Button(
    image=pause_img,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pauseVideo(),
    relief="flat"
)
pause_btn.place(
    x=450,
    y=420,
    width=50,
    height=30
)

# stop button
stop_img_old = Image.open('.\\pythonProject\\pics\\stop.jpg')
stop_img_resized = stop_img_old.resize((55, 65))
stop_img = ImageTk.PhotoImage(stop_img_resized)
stop_btn = Button(
    image=stop_img,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: stopVideo(),
    relief="flat"
)
stop_btn.place(
    x=525,
    y=420,
    width=50,
    height=30
)
############################################################

videoplayer = TkinterVideo(frame, scaled=True)
videoplayer.load(r"final output.mp4")
videoplayer.place(
    width=550,
    height=350
)
videoplayer.play()
    # else:
    #     print("no video entered")


# play video function
def playVideo():
    videoplayer.play()


# pause video function
def pauseVideo():
    videoplayer.pause()

global add,delete
add = False
delete = False

# stop video function
def stopVideo():
    videoplayer.stop()    

#add video function
def click_add_btn():
    add = True
    # delete = False
    gp.destroy()
    subprocess.call(["python", "Firebase.py"])

#delete video function
def click_del_btn():
    add = False
    # delete = True
    gp.destroy()
    subprocess.call(["python","Firebase.py"])
###########################################################
# back button function
def back_btn_clicked():
    gp.destroy()
    subprocess.call(["python", "CreateScreen.py"])


gp.mainloop()
