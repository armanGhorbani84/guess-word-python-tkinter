from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
# root.attributes('-fullscreen',True)

#DEF CORRECT
def correct():
    if a.get() == "word1":
        if entryword13.get() == "a" and entryword15.get() == "e":
            messagebox.showinfo("win","congratulations")
        else :
            messagebox.showerror("eror","wrong answer \n try again")
    elif a.get() == "word2":
        if entryword22.get() == "p" and entryword24.get() == "l":
            messagebox.showinfo("win","congratulations")
        else :
            messagebox.showerror("eror","wrong answer \n try again")
    elif a.get() == "word3":
        if entryword33.get() == "e" and entryword34.get() == "a":
            messagebox.showinfo("win","congratulations")
        else :
            messagebox.showerror("eror","wrong answer \n try again")
    elif a.get() == "word4":
        if entryword42.get() == "u" and entryword43.get() == "n" and entryword44.get() == "n":
            messagebox.showinfo("win","congratulations")
        else :
            messagebox.showerror("eror","wrong answer \n try again")
    elif a.get() == "word5":
        if entryword51.get() == "e" and entryword52.get() == "r" and entryword53.get() == "r":
            messagebox.showinfo("win","congratulations")
        else :
            messagebox.showerror("eror","wrong answer \n try again")
    elif a.get() == "word6":
        if entryword62.get() == "u" and entryword63.get() == "e" and entryword65.get() == "s":
            messagebox.showinfo("win","congratulations")
        else :
            messagebox.showerror("eror","wrong answer \n try again")

#DEF HINT
def hintword():
    if a.get() == "word1":
        if entryword13.get() == "":
            text3.set("a")
        elif entryword15.get() == "":
            text5.set("e")
        else:
            messagebox.showerror("eror","the whole blanks are fill \n first delete the letters")    
    elif a.get() == "word2":
        if entryword22.get() == "":
            text7.set("p")
        elif entryword24.get() == "":
            text9.set("l")
        else:
            messagebox.showerror("eror","the whole blanks are fill \n first delete the letters")     
    elif a.get() == "word3":
        if entryword33.get() == "":
            text13.set("e")
        elif entryword34.get() == "":
            text14.set("a")
        else:
            messagebox.showerror("eror","the whole blanks are fill \n first delete the letters") 
    elif a.get() == "word4":
        if entryword42.get() == "":
            text17.set("u")
        elif entryword43.get() == "":
            text18.set("n")
        elif entryword44.get() == "":
            text19.set("n")
        else:
            messagebox.showerror("eror","the whole blanks are fill \n first delete the letters") 
    elif a.get() == "word5":
        if entryword51.get() == "":
            text21.set("e")
        elif entryword52.get() == "":
            text22.set("r")
        elif entryword53.get() == "":
            text23.set("r")
        else:
            messagebox.showerror("eror","the whole blanks are fill \n first delete the letters") 
    elif a.get() == "word6":
        if entryword62.get() == "":
            text27.set("u")
        elif entryword63.get() == "":
            text28.set("e")
        elif entryword65.get() == "":
            text30.set("s")
        else:
            messagebox.showerror("eror","the whole blanks are fill \n first delete the letters") 

#IMAGE
img1 = ImageTk.PhotoImage(Image.open("stars.jpg"))
lablephoto = Label(image=img1)
lablephoto.pack()

img2 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
lablephoto = Label(image=img2)
lablephoto.place(x=100,y=200)

img3 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
lablephoto = Label(image=img3)
lablephoto.place(x=600,y=200)

img4 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
lablephoto = Label(image=img4)
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

text20 = StringVar()
text20.set("y")
entryword45 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text20,state="disabled")                    
entryword45.place(x=380,y=410,width=60,height=60)

################
text21 = StringVar()
text21.set("")
entryword51 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text21)                    
entryword51.place(x=110,y=475,width=60,height=60)

text22 = StringVar()
text22.set("")
entryword52 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text22)                    
entryword52.place(x=177,y=475,width=60,height=60)

text23 = StringVar()
text23.set("")
entryword53 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text23)                    
entryword53.place(x=245,y=475,width=60,height=60)

text24 = StringVar()
text24.set("o")
entryword54 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text24,state="disabled")                    
entryword54.place(x=313,y=475,width=60,height=60)

text25 = StringVar()
text25.set("r")
entryword55 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text25,state="disabled")                    
entryword55.place(x=380,y=475,width=60,height=60)

############
text26 = StringVar()
text26.set("G")
entryword61 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text26,state="disabled")                    
entryword61.place(x=110,y=545,width=60,height=60)

text27 = StringVar()
text27.set("")
entryword62 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text27)                    
entryword62.place(x=177,y=545,width=60,height=60)

text28 = StringVar()
text28.set("")
entryword63 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text28)                    
entryword63.place(x=245,y=545,width=60,height=60)

text29 = StringVar()
text29.set("s")
entryword64 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text29,state="disabled")                    
entryword64.place(x=313,y=545,width=60,height=60)

text30 = StringVar()
text30.set("")
entryword65 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text30)                    
entryword65.place(x=380,y=545,width=60,height=60)


#LABLE



#RADIO BUTTON 
a=StringVar()
a.set(True)

rb1=Radiobutton(root,variable=a,value="word1")
rb1.place(x=460,y=220)

rb2=Radiobutton(root,variable=a,value="word2")
rb2.place(x=460,y=290)

rb3=Radiobutton(root,variable=a,value="word3")
rb3.place(x=460,y=360)

rb4=Radiobutton(root,variable=a,value="word4")
rb4.place(x=460,y=430)

rb5=Radiobutton(root,variable=a,value="word5")
rb5.place(x=460,y=500)

rb6=Radiobutton(root,variable=a,value="word6")
rb6.place(x=460,y=570)

#BUTTON
btn = Button(root,text="Check Answer",command=correct,font=('Georgia 15'))
btn.place(x=120,y=650)

btnHint = Button(root,text="Hint",command=hintword,font=('Georgia 15'))
btnHint.place(x=120,y=695)


root.mainloop()