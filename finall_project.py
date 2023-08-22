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
            lable1 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable1.place(x=50,y=215)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable1 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable1.place(x=50,y=215)
    elif a.get() == "word2":
        if entryword22.get() == "p" and entryword24.get() == "l":
            messagebox.showinfo("win","congratulations")
            lable2 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable2.place(x=50,y=280)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable2 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable2.place(x=50,y=280)
    elif a.get() == "word3":
        if entryword33.get() == "e" and entryword34.get() == "a":
            messagebox.showinfo("win","congratulations")
            lable3 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable3.place(x=50,y=350)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable3 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable3.place(x=50,y=350)
    elif a.get() == "word4":
        if entryword42.get() == "u" and entryword43.get() == "n" and entryword44.get() == "n":
            messagebox.showinfo("win","congratulations")
            lable4 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable4.place(x=50,y=420)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable4 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable4.place(x=50,y=420)
    elif a.get() == "word5":
        if entryword51.get() == "e" and entryword52.get() == "r" and entryword53.get() == "r":
            messagebox.showinfo("win","congratulations")
            lable5 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable5.place(x=50,y=485)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable5 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable5.place(x=50,y=485)
    elif a.get() == "word6":
        if entryword62.get() == "u" and entryword63.get() == "e" and entryword65.get() == "s":
            messagebox.showinfo("win","congratulations")
            lable6 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable6.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable6 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable6.place(x=50,y=550)
    #######
    elif a.get() == "word7":
        if entryword72.get() == "a" and entryword73.get() == "r":
            messagebox.showinfo("win","congratulations")
            lable7 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable7.place(x=20,y=20)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable7 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable7.place(x=20,y=20)
    elif a.get() == "word8":
        if entryword81.get() == "f" and entryword85.get() == "t":
            messagebox.showinfo("win","congratulations")
            lable8 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable8.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable8 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable8.place(x=50,y=550)
    elif a.get() == "word9":
        if entryword94.get() == "e" and entryword95.get() == "o":
            messagebox.showinfo("win","congratulations")
            lable9 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable9.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable9= Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable9.place(x=50,y=550)
    elif a.get() == "word10":
        if entryword102.get() == "a" and entryword104.get() == "e":
            messagebox.showinfo("win","congratulations")
            lable10 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable10.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable10= Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable10.place(x=50,y=550)
    elif a.get() == "word11":
        if entryword113.get() == "i" and entryword114.get() == "l" and entryword115.get() == "l":
            messagebox.showinfo("win","congratulations")
            lable11 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable11.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable11 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable11.place(x=50,y=550)
    elif a.get() == "word12":
        if entryword121.get() == "p" and entryword122.get() == "o":
            messagebox.showinfo("win","congratulations")
            lable12 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable12.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable12 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable12.place(x=50,y=550)
    #########
    elif a.get() == "word13":
        if entryword133.get() == "i" and entryword135.get() == "e":
            messagebox.showinfo("win","congratulations")
            lable13 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable13.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable13 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable13.place(x=50,y=550)
    elif a.get() == "word14":
        if entryword143.get() == "e" and entryword144.get() == "a":
            messagebox.showinfo("win","congratulations")
            lable14 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable14.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable14 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable14.place(x=50,y=550)
    elif a.get() == "word15":
        if entryword151.get() == "a" and entryword152.get() == "c":
            messagebox.showinfo("win","congratulations")
            lable15 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable15.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable15 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable15.place(x=50,y=550)
    elif a.get() == "word16":
        if entryword164.get() == "l" and entryword165.get() == "t":
            messagebox.showinfo("win","congratulations")
            lable16 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable16.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable16 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable16.place(x=50,y=550)
    elif a.get() == "word17":
        if entryword171.get() == "b" and entryword172.get() == "l":
            messagebox.showinfo("win","congratulations")
            lable17 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable17.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable17 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable17.place(x=50,y=550)
    elif a.get() == "word18":
        if entryword183.get() == "i" and entryword185.get() == "e":
            messagebox.showinfo("win","congratulations")
            lable18 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable18.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable18 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable18.place(x=50,y=550)
    elif a.get() == "word19":
        if entryword192.get() == "r" and entryword193.get() == "o" and entryword194.get() == "n":
            messagebox.showinfo("win","congratulations")
            lable19 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable19.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable19 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable19.place(x=50,y=550)
    elif a.get() == "word20":
        if entryword202.get() == "h" and entryword204.get() == "p":
            messagebox.showinfo("win","congratulations")
            lable20 = Label(root,text="✅",font=('Georgia 25'),justify="center")
            lable20.place(x=50,y=550)
        else :
            messagebox.showerror("eror","wrong answer \n try again")
            lable20 = Label(root,text="❌",font=('Georgia 25'),justify="center")
            lable20.place(x=50,y=550)
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

# img2 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
# lablephoto = Label(image=img2)
# lablephoto.place(x=100,y=200)

# img3 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
# lablephoto = Label(image=img3)
# lablephoto.place(x=600,y=200)

# img4 = ImageTk.PhotoImage(Image.open("gamenowpixel.png"))
# lablephoto = Label(image=img4)
# lablephoto.place(x=1100,y=200)

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
######################

text31 = StringVar()
text31.set("E")
entryword71 = Entry(root,font=('Georgia 40'),justify="center",state="disabled",textvariable = text31)                    
entryword71.place(x=610,y=205,width=60,height=60)

text32 = StringVar()
text32.set("")
entryword72 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text32)                    
entryword72.place(x=675,y=205,width=60,height=60)

text33 = StringVar()
text33.set("")
entryword73 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text33)                    
entryword73.place(x=745,y=205,width=60,height=60)

text34 = StringVar()
text34.set("t")
entryword74 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text34,state="disabled")                    
entryword74.place(x=812,y=205,width=60,height=60)

text35 = StringVar()
text35.set("h")
entryword75 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text35,state="disabled")                    
entryword75.place(x=880,y=205,width=60,height=60)
#########

text36 = StringVar()
text36.set("")
entryword81 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text36)                    
entryword81.place(x=610,y=275,width=60,height=60)

text37 = StringVar()
text37.set("r")
entryword82 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text37,state="disabled")                    
entryword82.place(x=675,y=275,width=60,height=60)

text38 = StringVar()
text38.set("u")
entryword83 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text38,state="disabled")                    
entryword83.place(x=745,y=275,width=60,height=60)

text39 = StringVar()
text39.set("i")
entryword84 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text39,state="disabled")                    
entryword84.place(x=812,y=275,width=60,height=60)

text40 = StringVar()
text40.set("")
entryword85 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text40)                    
entryword85.place(x=880,y=275,width=60,height=60)
############
text41 = StringVar()
text41.set("V")
entryword91 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text41,state="disabled")                    
entryword91.place(x=610,y=340,width=60,height=60)

text42 = StringVar()
text42.set("i")
entryword92 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text42,state="disabled")                    
entryword92.place(x=675,y=340,width=60,height=60)

text43 = StringVar()
text43.set("d")
entryword93 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text43,state="disabled")                    
entryword93.place(x=745,y=340,width=60,height=60)

text44 = StringVar()
text44.set("")
entryword94 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text44)                    
entryword94.place(x=812,y=340,width=60,height=60)

text45 = StringVar()
text45.set("")
entryword95 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text45)                    
entryword95.place(x=880,y=340,width=60,height=60)
##########
text46 = StringVar()
text46.set("W")
entryword101 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text46,state="disabled")                    
entryword101.place(x=610,y=410,width=60,height=60)

text47 = StringVar()
text47.set("")
entryword102 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text47)                    
entryword102.place(x=675,y=410,width=60,height=60)

text48 = StringVar()
text48.set("t")
entryword103 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text48,state="disabled")                    
entryword103.place(x=745,y=410,width=60,height=60)

text49 = StringVar()
text49.set("")
entryword104 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text49)                    
entryword104.place(x=812,y=410,width=60,height=60)

text50 = StringVar()
text50.set("r")
entryword105 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text50,state="disabled")                    
entryword105.place(x=880,y=410,width=60,height=60)
########
text51 = StringVar()
text51.set("S")
entryword111 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text51,state="disabled")                    
entryword111.place(x=610,y=475,width=60,height=60)

text52 = StringVar()
text52.set("k")
entryword112 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text52,state="disabled")                    
entryword112.place(x=675,y=475,width=60,height=60)

text53 = StringVar()
text53.set("")
entryword113 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text53)                    
entryword113.place(x=745,y=475,width=60,height=60)

text54 = StringVar()
text54.set("")
entryword114 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text54)                    
entryword114.place(x=812,y=475,width=60,height=60)

text55 = StringVar()
text55.set("")
entryword115 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text55)                    
entryword115.place(x=880,y=475,width=60,height=60)
#########
text56 = StringVar()
text56.set("")
entryword121 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text56)                    
entryword121.place(x=610,y=545,width=60,height=60)

text57 = StringVar()
text57.set("")
entryword122 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text57)                    
entryword122.place(x=675,y=545,width=60,height=60)

text58 = StringVar()
text58.set("w")
entryword123 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text58,state="disabled")                    
entryword123.place(x=745,y=545,width=60,height=60)

text59 = StringVar()
text59.set("e")
entryword124 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text59,state="disabled")                    
entryword124.place(x=812,y=545,width=60,height=60)

text60 = StringVar()
text60.set("r")
entryword125 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text60,state="disabled")                    
entryword125.place(x=880,y=545,width=60,height=60)
##########
text61 = StringVar()
text61.set("P")
entryword131 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text61,state="disabled")                    
entryword131.place(x=1110,y=205,width=60,height=60)

text62 = StringVar()
text62.set("r")
entryword132 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text62,state="disabled")                    
entryword132.place(x=1177,y=205,width=60,height=60)

text63 = StringVar()
text63.set("")
entryword133 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text63)                    
entryword133.place(x=1245,y=205,width=60,height=60)

text64 = StringVar()
text64.set("c")
entryword134 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text64,state="disabled")                    
entryword134.place(x=1313,y=205,width=60,height=60)

text65 = StringVar()
text65.set("")
entryword135 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text65)                    
entryword135.place(x=1380,y=205,width=60,height=60)
###########
text66 = StringVar()
text66.set("O")
entryword141 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text66,state="disabled")                    
entryword141.place(x=1110,y=275,width=60,height=60)

text67 = StringVar()
text67.set("c")
entryword142 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text67,state="disabled")                    
entryword142.place(x=1177,y=275,width=60,height=60)

text68 = StringVar()
text68.set("")
entryword143 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text68)                    
entryword143.place(x=1245,y=275,width=60,height=60)

text69 = StringVar()
text69.set("")
entryword144 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text69)                    
entryword144.place(x=1313,y=275,width=60,height=60)

text70 = StringVar()
text70.set("n")
entryword145 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text70,state="disabled")                    
entryword145.place(x=1380,y=275,width=60,height=60)
##########
text71 = StringVar()
text71.set("")
entryword151 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text71)                    
entryword151.place(x=1110,y=345,width=60,height=60)

text72 = StringVar()
text72.set("")
entryword152 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text72)                    
entryword152.place(x=1177,y=345,width=60,height=60)

text73 = StringVar()
text73.set("t")
entryword153 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text73,state="disabled")                    
entryword153.place(x=1245,y=345,width=60,height=60)

text74 = StringVar()
text74.set("o")
entryword154 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text74,state="disabled")                    
entryword154.place(x=1313,y=345,width=60,height=60)

text75 = StringVar()
text75.set("r")
entryword155 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text75,state="disabled")                    
entryword155.place(x=1380,y=345,width=60,height=60)
#######

text76 = StringVar()
text76.set("A")
entryword161 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text76,state="disabled")                    
entryword161.place(x=1110,y=415,width=60,height=60)

text77 = StringVar()
text77.set("d")
entryword162 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text77,state="disabled")                    
entryword162.place(x=1177,y=415,width=60,height=60)

text78 = StringVar()
text78.set("u")
entryword163 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text78,state="disabled")                    
entryword163.place(x=1245,y=415,width=60,height=60)

text79 = StringVar()
text79.set("")
entryword164 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text79)                    
entryword164.place(x=1313,y=415,width=60,height=60)

text80 = StringVar()
text80.set("")
entryword165 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text80)                    
entryword165.place(x=1380,y=415,width=60,height=60)
#######

text81 = StringVar()
text81.set("")
entryword171 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text81)                    
entryword171.place(x=1110,y=485,width=60,height=60)

text82 = StringVar()
text82.set("")
entryword172 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text82)                    
entryword172.place(x=1177,y=485,width=60,height=60)

text83 = StringVar()
text83.set("a")
entryword173 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text83,state="disabled")                    
entryword173.place(x=1245,y=485,width=60,height=60)

text84 = StringVar()
text84.set("c")
entryword174 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text84,state="disabled")                    
entryword174.place(x=1313,y=485,width=60,height=60)

text85 = StringVar()
text85.set("k")
entryword175 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text85,state="disabled")                    
entryword175.place(x=1380,y=485,width=60,height=60)
########

text86 = StringVar()
text86.set("W")
entryword181 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text86,state="disabled")                    
entryword181.place(x=1110,y=555,width=60,height=60)

text87 = StringVar()
text87.set("h")
entryword182 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text87,state="disabled")                    
entryword182.place(x=1177,y=555,width=60,height=60)

text88 = StringVar()
text88.set("")
entryword183 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text88)                    
entryword183.place(x=1245,y=555,width=60,height=60)

text89 = StringVar()
text89.set("l")
entryword184 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text89,state="disabled")                    
entryword184.place(x=1313,y=555,width=60,height=60)

text90 = StringVar()
text90.set("")
entryword185 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text90)                    
entryword185.place(x=1380,y=555,width=60,height=60)
#######

text91 = StringVar()
text91.set("W")
entryword191 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text91,state="disabled")                    
entryword191.place(x=110,y=135,width=60,height=60)

text92 = StringVar()
text92.set("")
entryword192 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text92)                    
entryword192.place(x=177,y=135,width=60,height=60)

text93 = StringVar()
text93.set("")
entryword193 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text93)                    
entryword193.place(x=245,y=135,width=60,height=60)

text94 = StringVar()
text94.set("")
entryword194 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text94)                    
entryword194.place(x=313,y=135,width=60,height=60)

text95 = StringVar()
text95.set("g")
entryword195 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text95,state="disabled")                    
entryword195.place(x=380,y=135,width=60,height=60)
#######

text96 = StringVar()
text96.set("s")
entryword201 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text96,state="disabled")                    
entryword201.place(x=610,y=135,width=60,height=60)

text97 = StringVar()
text97.set("")
entryword202 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text97)                    
entryword202.place(x=675,y=135,width=60,height=60)

text98 = StringVar()
text98.set("a")
entryword203 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text98,state="disabled")                    
entryword203.place(x=745,y=135,width=60,height=60)

text99 = StringVar()
text99.set("")
entryword204 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text99)                    
entryword204.place(x=812,y=135,width=60,height=60)

text100 = StringVar()
text100.set("e")
entryword205 = Entry(root,font=('Georgia 40'),justify="center",textvariable = text100,state="disabled")                    
entryword205.place(x=880,y=135,width=60,height=60)

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
######
rb7=Radiobutton(root,variable=a,value="word7")
rb7.place(x=960,y=220)

rb8=Radiobutton(root,variable=a,value="word8")
rb8.place(x=960,y=290)

rb9=Radiobutton(root,variable=a,value="word9")
rb9.place(x=960,y=360)

rb10=Radiobutton(root,variable=a,value="word10")
rb10.place(x=960,y=430)

rb11=Radiobutton(root,variable=a,value="word11")
rb11.place(x=960,y=500)

rb12=Radiobutton(root,variable=a,value="word12")
rb12.place(x=960,y=570)
########
rb13=Radiobutton(root,variable=a,value="word13")
rb13.place(x=1460,y=220)

rb14=Radiobutton(root,variable=a,value="word14")
rb14.place(x=1460,y=290)

rb15=Radiobutton(root,variable=a,value="word15")
rb15.place(x=1460,y=360)

rb16=Radiobutton(root,variable=a,value="word16")
rb16.place(x=1460,y=430)

rb17=Radiobutton(root,variable=a,value="word17")
rb17.place(x=1460,y=500)

rb18=Radiobutton(root,variable=a,value="word18")
rb18.place(x=1460,y=570)

rb19=Radiobutton(root,variable=a,value="word19")
rb19.place(x=460,y=150)

rb20=Radiobutton(root,variable=a,value="word20")
rb20.place(x=960,y=150)


#BUTTON
btn = Button(root,text="Check Answer",command=correct,font=('Georgia 15'))
btn.place(x=120,y=650)

btnHint = Button(root,text="Hint",command=hintword,font=('Georgia 15'))
btnHint.place(x=120,y=695)

root.mainloop()