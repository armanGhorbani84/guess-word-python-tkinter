from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
# root.attributes('-fullscreen',True)

#DEF CORRECT
def correctword1():
    if entryword13.get()=="a" and entryword15.get()=="e":
        messagebox.showinfo("correct","congratulations")
    else :
        messagebox.showerror("eror","wrong answer \n try again")
def correctword2():
    if entryword22.get()=="p" and entryword24.get()=="l":
        messagebox.showinfo("correct","congratulations")
    else :
        messagebox.showerror("eror","wrong answer \n try again")
def correctword3():
    if entryword33.get()=="e" and entryword34.get()=="a":
        messagebox.showinfo("correct","congratulations")
    else :
        messagebox.showerror("eror","wrong answer \n try again")
def correctword4():
    if entryword42.get()=="u" and entryword43.get()=="n" and entryword44.get()=="n":
        messagebox.showinfo("correct","congratulations")
    else :
        messagebox.showerror("eror","wrong answer \n try again")

#DEF HINT
def hintword1():
        if entryword13.get()=="" :
            text3.set("a") 
        elif entryword15.get()=="":
             text5.set("e")
        else :
             messagebox.showerror("eror","the whole blanks are fill \n first delete the letters :) ")
def hintword2():
        if entryword22.get()=="" :
            text7.set("p") 
        elif entryword24.get()=="":
             text9.set("l")
        else :
             messagebox.showerror("eror","the whole blanks are fill \n first delete the letters :) ")
def hintword3():
        if entryword33.get()=="" :
            text13.set("e") 
        elif entryword34.get()=="":
             text14.set("a")
        else :
             messagebox.showerror("eror","the whole blanks are fill \n first delete the letters :) ")        
def hintword4():
        if entryword42.get()=="" :
            text17.set("u") 
        elif entryword43.get()=="":
             text18.set("n")
        elif entryword44.get()=="":
             text19.set("n")
        else :
             messagebox.showerror("eror","the whole blanks are fill \n first delete the letters :) ")       
    

#IMAGE
img5 = ImageTk.PhotoImage(Image.open("nature1.jpg"))
lablephoto = Label(image=img5)
lablephoto.pack()

img1 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
lablephoto = Label(image=img1)
lablephoto.place(x=100,y=200)

img2 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
lablephoto = Label(image=img2)
lablephoto.place(x=600,y=200)

img3 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
lablephoto = Label(image=img3)
lablephoto.place(x=1100,y=200)

#ENTRY
text1 = StringVar()
text1.set("P")
entryword11 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text1)                    
entryword11.place(x=110,y=205,width=60,height=60)

text2 = StringVar()
text2.set("l")
entryword12 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text2)                    
entryword12.place(x=177,y=205,width=60,height=60)

text3 = StringVar()
text3.set("")
entryword13 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text3)                    
entryword13.place(x=245,y=205,width=60,height=60)

text4 = StringVar()
text4.set("c")
entryword14 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text4)                    
entryword14.place(x=313,y=205,width=60,height=60)

text5 = StringVar()
text5.set("")
entryword15 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text5)                    
entryword15.place(x=380,y=205,width=60,height=60)

####################
text6 = StringVar()
text6.set("A")
entryword21 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text6)                    
entryword21.place(x=110,y=275,width=60,height=60)

text7 = StringVar()
text7.set("")
entryword22 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text7)                    
entryword22.place(x=177,y=275,width=60,height=60)

text8 = StringVar()
text8.set("p")
entryword23 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text8,state="disabled")                    
entryword23.place(x=245,y=275,width=60,height=60)

text9 = StringVar()
text9.set("")
entryword24 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text9)                    
entryword24.place(x=313,y=275,width=60,height=60)

text10 = StringVar()
text10.set("e")
entryword25 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text10,state="disabled")                    
entryword25.place(x=380,y=275,width=60,height=60)

####################
text11 = StringVar()
text11.set("C")
entryword31 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text11)                    
entryword31.place(x=110,y=340,width=60,height=60)

text12 = StringVar()
text12.set("l")
entryword32 = Entry(root,font=('Georgia 40'),state="disabled",justify="center",textvariable = text12)                    
entryword32.place(x=177,y=340,width=60,height=60)

text13 = StringVar()
text13.set("")
entryword33 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text13)                    
entryword33.place(x=245,y=340,width=60,height=60)

text14 = StringVar()
text14.set("")
entryword34 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text14)                    
entryword34.place(x=313,y=340,width=60,height=60)

text15 = StringVar()
text15.set("n")
entryword35 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text15,state="disabled")                    
entryword35.place(x=380,y=340,width=60,height=60)

####################
text16 = StringVar()
text16.set("F")
entryword41 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text16)                    
entryword41.place(x=110,y=410,width=60,height=60)

text17 = StringVar()
text17.set("")
entryword42 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text17)                    
entryword42.place(x=177,y=410,width=60,height=60)

text18 = StringVar()
text18.set("")
entryword43 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text18)                    
entryword43.place(x=245,y=410,width=60,height=60)

text19 = StringVar()
text19.set("")
entryword44 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text19)                    
entryword44.place(x=313,y=410,width=60,height=60)

texttwenty = StringVar()
texttwenty.set("y")
entryword45 = Entry(root,font=('Georgia 40'),justify="center",textvariable = texttwenty,state="disabled")                    
entryword45.place(x=380,y=410,width=60,height=60)


#LABLE



#BUTTON 
buttonword11 = Button(root,text="answer",command=correctword1,bg="black",fg="white",font="arial",cursor="hand2")
buttonword11.place(x=460,y=205,width=90,height=30)
hintword12= Button(root,text="hint",command=hintword1,bg="black",fg="white",font="arial",cursor="hand2")
hintword12.place(x=460,y=235,width=90,height=30)

buttonword21= Button(root,text="answer",command=correctword2,bg="black",fg="white",font="arial",cursor="hand2")
buttonword21.place(x=460,y=275,width=90,height=30)
hintword22= Button(root,text="hint",command=hintword2,bg="black",fg="white",font="arial",cursor="hand2")
hintword22.place(x=460,y=305,width=90,height=30)

buttonword31= Button(root,text="answer",command=correctword3,bg="black",fg="white",font="arial",cursor="hand2")
buttonword31.place(x=460,y=345,width=90,height=30)
hintword32= Button(root,text="hint",command=hintword3,bg="black",fg="white",font="arial",cursor="hand2")
hintword32.place(x=460,y=375,width=90,height=30)

buttonword41= Button(root,text="answer",command=correctword4,bg="black",fg="white",font="arial",cursor="hand2")
buttonword41.place(x=460,y=415,width=90,height=30)
hintword42= Button(root,text="hint",command=hintword4,bg="black",fg="white",font="arial",cursor="hand2")
hintword42.place(x=460,y=445,width=90,height=30)

root.mainloop()


#test