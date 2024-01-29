import subprocess
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
from tkVideoPlayer import TkinterVideo
from PIL import Image, ImageTk
from demo import *
from skimage import img_as_ubyte
import numpy
import moviepy.editor as mp


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

frame_1 = Frame(gp, width=300, height=290)
frame_1.place(
    x=170,
    y=20
)
frame_2 = Frame(gp, width=300, height=290)
frame_2.place(
    x=500,
    y=20
)

# upload video button
upVideo = Button(
    text='Upload Video',
    font=18,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: buVideoClicked(),
    relief="flat"
)
upVideo.place(
    x=215,
    y=355,
    width=200,
    height=40
)

# upload image button
upImg = Button(
    text='Upload Image',
    font=18,
    bg='#4a148c',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: buImgClicked(),
    relief="flat"
)
upImg.place(
    x=550,
    y=355,
    width=200,
    height=40
)

# generate button
generate_img_old = Image.open('.\\pythonProject\\pics\\generate-button-hi.png')
generate_img_resized = generate_img_old.resize((150, 65))
generate_img = ImageTk.PhotoImage(generate_img_resized)
generate = Button(
    image=generate_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_btn_click(),
    relief="flat"
)
generate.place(
    x=410,
    y=450,
    width=150,
    height=65
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
    x=215,
    y=315,
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
    x=290,
    y=315,
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
    x=365,
    y=315,
    width=50,
    height=30
)


# upload video button click
def buVideoClicked():
    open_video()


# upload image button click
def buImgClicked():
    open_image()

# def resize1(image, size=(256, 256)):
# 	w, h = image.size
# 	d = min(w, h)
# 	r = ((w - d) // 2, (h - d) // 2, (w + d) // 2, (h + d) // 2)
# 	return image.resize(size, resample=PIL.Image.LANCZOS, box=r)

# function that get the image and validate
def open_image():
    global img,img1
    f_types = [('Image Files', '*.jpg'), ('Image Files', '*.png')]
    file_name = askopenfilename(filetypes=f_types)
    if file_name is not None:
        img_old = Image.open(file_name)
        print(img_old.format)

        img_old_resized = img_old.resize((300, 300))
        # img_old_resized = resize(PIL.Image.open(io.BytesIO(img_old)).convert("RGB"))
        img1 = numpy.array(img_old)
        img = ImageTk.PhotoImage(img_old_resized)
        label = Label(frame_2, image=img)
        label.pack()
        
    # print(img.__format__)
    # print(img.size)  
    # print(img.mode)
    print(type(img1))
 
    #  shape
    print(img1.shape)  

    # img = resize(img,(256,256))[...,3]
    # img = img[numpy.newaxis,...]
    # img = resize1(PIL.Image.open(io.BytesIO(img)).convert("RGB"))
# function that get the video and validate


def open_video():
    file = askopenfile(mode='r', filetypes=[('Video files', ["*.mp4"])])
    
    if file is not None:
        global filename
        filename = file.name
        video = mp.VideoFileClip(filename)
        video.audio.write_audiofile("voice output.mp3")

        global videoplayer
        videoplayer = TkinterVideo(frame_1, scaled=True)
        videoplayer.load(r"{}".format(filename))
        # videoplayer = ffmpeg.input(r"{}".format(filename))
        videoplayer.place(
            width=300,
            height=290
        )
        
        videoplayer.play()
        
    else:
        print("no video entered")


def generate():
    reader = imageio.get_reader(filename, mode='I', format='FFMPEG')
    fps = reader.get_meta_data()['fps']
    driving_video = []

    for frame in reader:
        driving_video.append(frame)
    generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', checkpoint_path='config/vox-cpk.pth.tar',cpu = True)
    
    # img1 = skimage.transform.resize(numpy.asarray(img), (256, 256))
    # [skimage.transform.resize(frame, (256, 256)) for frame in driving_video]
    driving_video = [resize(frame,(256,256))[...,:3] for frame in driving_video]

    # img0 = ImageTk.PhotoImage(image=Image.fromarray(img))

    img2 = resize(img1,(256,256))[...,:3]
    # ffmpeg.output(ffmpeg.input('output.mp4').video, ffmpeg.input(driving_video).audio, output.name, c='copy').overwrite_output().run()

    predictions = make_animation(img2, driving_video, generator, kp_detector,cpu=True)
    
    imageio.mimsave('output.mp4', [img_as_ubyte(frame) for frame in predictions], fps=fps)
    # ffmpeg.output(ffmpeg.input('output.mp4').video, ffmpeg.input(driving_video).audio, output.name,c='copy').overwrite_output().run()
    # predictions = ffmpeg.input('output.mp4').video
    # predictions = ffmpeg.input(driving_video).audio
    clip = mp.VideoFileClip("output.mp4")
    audio_backgroung = mp.AudioFileClip("voice output.mp3")
    # final_audio = mp.CompositeAudioClip([audio_backgroung,clip.audio])
    final_clip = clip.set_audio(audio_backgroung)
    print("##################################################")
    final_clip.write_videofile("final output.mp4")
    
                
    return predictions

# play video function
def playVideo():
    videoplayer.play()


# pause video function
def pauseVideo():
    videoplayer.pause()


# stop video function
def stopVideo():
    videoplayer.stop()


# generate button click
def generate_btn_click():
    generate()
    gp.destroy()
    subprocess.call(["python", "UploadScreen.py"])
    

gp.mainloop()
