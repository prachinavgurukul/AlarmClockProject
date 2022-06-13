from time import strftime   
from tkinter import * 
import time
import datetime
from turtle import width
from pygame import mixer
root = Tk() #It helps to display the root window and manages all the other components of the tkinter application
root.title('Alarm Clock') 
def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 
def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 18, 'bold'),
            text="Wake up!Wake up!Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=5)
            print("wake up!")
            mixer.init()
            mixer.music.load('/home/jijasarak/Downloads/tone (1).mp3')
            mixer.music.play()
            break
hrs=StringVar()
mins=StringVar()
secs=StringVar()
greet=Label(root, font = ('arial', 20, 'bold'),
text="ALARM CLOCK").grid(row=1,columnspan=4)
clockimg=PhotoImage(file="/home/jijasarak/Downloads/mostafa-mahmoudi-Qy_F1Wqw6Ho-unsplash.png")
img=Label(root,image=clockimg)
img.grid(rowspan=4,column=0)
hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold'))
hrbtn.grid(row=2,column=1)
minbtn=Entry(root,textvariable=mins,width=5,font = ('arial', 20, 'bold')).grid(row=2,column=2)
secbtn=Entry(root,textvariable=secs,width=5,font = ('arial', 20, 'bold')).grid(row=2,column=3)
setbtn=Button(root,text="Set Alarm",command=setalarm,bg="DodgerBlue2",
fg="black",font = ('arial', 20, 'bold')).grid(row=4,column=1,columnspan=5)
timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid()
mainloop() 
            