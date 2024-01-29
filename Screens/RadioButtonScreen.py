from tkinter import *
import subprocess
import tkinter

rad = Tk()
rad.geometry("500x400+300+150")

#Background
bgImg = tkinter.PhotoImage(file='.\\pythonProject\\pics\\background.png')
bg = Label(rad, image=bgImg)
bg.place(
    width=1000,
    height=600
)
#title
l = Label(text = "Select Folder",width=50,height=1,font=("Helvetica", 16),background="#4a148c",foreground="black")
l.pack()

#Get video name
label1 = Label(rad,text="Enter video name:",fg="white",bg="#4a148c",font=('Arial',10,'bold'))
label1.place(x=50,y=50)

global data
data = StringVar()
my_text = Entry(rad,textvariable=data)
my_text.place(x=180,y=51)


#Choose Video Folder
var = IntVar()
r1 = Radiobutton(rad,text="Cleoptra",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=1)
r1.place(x=50,y=100)
r2 = Radiobutton(rad,text="Hatshepsut",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=2)
r2.place(x=50,y=130)
r3 = Radiobutton(rad,text="Nafrat",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=3)
r3.place(x=50,y=160)
r4 = Radiobutton(rad,text="Nefertiti",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=4)
r4.place(x=50,y=190)
r5 = Radiobutton(rad,text="Egyption Writer",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=5)
r5.place(x=350,y=100)
r6 = Radiobutton(rad,text="Menkaure",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=6)
r6.place(x=350,y=130)
r7 = Radiobutton(rad,text="Thutmose III",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=7)
r7.place(x=350,y=160)
r8 = Radiobutton(rad,text="Ra hotep",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=8)
r8.place(x=350,y=190)
r9 = Radiobutton(rad,text="Kaaper",background="#4a148c",foreground="black",font=('Arial',10,'bold'),variable=var,value=9)
r9.place(x=200,y=220)



choice = ""
# global videoName
def click_button():
    global foldername
    foldername = ""
    if var.get()== 1:
        choice = "Celopatra"
    elif var.get()== 2:
        choice = "Hatshepsut"
    elif var.get()== 3:
        choice = "Nafrat"
    elif var.get()== 4:
        choice = "Nefertiti"
    elif var.get()== 5:
        choice = "Egyption Writer"
    elif var.get()== 6:
        choice = "Menkaure"
    elif var.get()== 7:
        choice = "King Thutmose III"
    elif var.get()== 8:
        choice = "Ra"
    elif var.get()== 9:
        choice = "kaapar"
    # print("Folder is: "+choice," and the name is: "+ data.get())
    foldername = choice
    # print(foldername)
    rad.destroy()
    

# print("choice: "+choice)
submit = Button(rad,text="submit choice",fg="white",bg="#4a148f",command=click_button)
submit.place(x=190,y=280)


rad.mainloop()