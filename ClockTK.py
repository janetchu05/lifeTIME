import tkinter as tk
from tkinter import Canvas, messagebox
import datetime
from datetime import datetime
from random import *


def digitalClock():
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    s = now.strftime("%S")

    if int(h) >= 12 and int(h) < 24 and int(m) >= 0:
        Campm.config(text = "PM")
    else:
        Campm.config(text = "AM")
    if int(h) > 12:
        h = str((int(h) - 12))
    elif int(h) == 0:
        h = '12'
    
    Chour.config(text = h.zfill(2))
    Cminute.config(text = m.zfill(2))
    Csecond.config(text = s.zfill(2))

    
btnStatus = False
##Calculate Start BTN
def btnOK_Click():
    global btnStatus
    if btnStatus == False:
        btnStatus = True
    else :
        btnStatus = False

    if entYear.get() == '' or entMonth.get() == '' or entDay.get() == '':
        messagebox.showinfo("Error", "Entry is Empty. Please Type in your Birthdate")
    else:
        global ctr
        ctr = 0
        showProgress()


ctr = 0
##show Progress
def showProgress():
    if btnStatus == True :
        global ctr
        ctr += 1
        hour.config(text = randint(10, 99))
        minute.config(text = randint(10, 99))
        second.config(text = randint(10, 99))

        window.after(40, showProgress)
        if ctr > 30:
            showResult()



def showResult():
    #오늘 날짜
    now = datetime.now()
    #생년월일
    myYear = entYear.get()
    if int(myYear) < 100 :
        myYear = "19" + myYear
    myMonth = entMonth.get().strip("0")
    myDay = entDay.get().strip("0")
    myBirth = datetime(int(myYear), int(myMonth), int(myDay), 0, 0, 0)

    dayCount = (now - myBirth).days
    totalSec = (dayCount / 32828) * 86400

    myHour = int(totalSec // 3600)
    totalSec -= myHour * 3600
    myMinute = int(totalSec // 60)
    mySecond = int(totalSec - myMinute*60)

    if myHour >= 12 and myHour < 24 and myMinute >= 0:
        ampm.config(text = "PM")
    else :
        ampm.config(text = "AM")
    
    if myHour > 12 :
        myHour -= 12
    elif myHour == 0:
        myHour = 12

    hour.config(text = str(myHour).zfill(2))
    minute.config(text = str(myMinute).zfill(2))
    second.config(text = str(mySecond).zfill(2))
    global btnStatus
    btnStatus = False

    
def startTimer():
    window.after(1000, startTimer)
    digitalClock()
    


##윈도우 디자인
window = tk.Tk()

window.title("My lifeTIME")
window.geometry("700x500+100+100")
window.resizable(False, False)
window.config(bg = "black")

lblFirst = tk.Label(window, text = "Life is never late\n What is your time?\n\n", font = ('Digital-7 15 bold'), bg = "black", fg = "white")
lblFirst.pack(side = "top", pady = (50, 5))

lblDate = tk.Label(window, text = "Type in your BIRTHDATE", font = ('Digital-7 13 bold'), bg = "black", fg = "white")
lblDate.pack(side = "top", pady = 3)

##input frame
FrmInput = tk.Frame(window)
FrmInput.pack(side = "top", pady = 5)

entYear = tk.Entry(FrmInput, bd = 1, width = '7',font = ('Digital-7 13 bold'), bg = "black", fg = "white")
entYear.pack(side = "left")
tk.Label(FrmInput, text = " 년 ", font = ('Digital-7 13 bold'), bg = "black", fg = "white").pack(side = "left")

entMonth = tk.Entry(FrmInput, bd = 1, width = 5, font = ('Digital-7 13 bold'), bg = "black", fg = "white")
entMonth.pack(side = "left")
tk.Label(FrmInput, text = " 월 ", font = ('Digital-7 13 bold'), bg = "black", fg = "white").pack(side = "left")

entDay = tk.Entry(FrmInput, bd = 1, width = 5, font = ('Digital-7 13 bold'), bg = "black", fg = "white")
entDay.pack(side = "left")
tk.Label(FrmInput, text = " 일 ", font = ('Digital-7 13 bold'), bg = "black", fg = "white").pack(side = "left")


btnOK = tk.Button(window, text = "check your time", command = btnOK_Click, width = 40, font = ('Digital-7 13 bold'), bg = "white", fg = "black")
btnOK.pack(side = "top", pady = (10, 20))


##Clock
canvas = Canvas(window, width = 600, height = 200, bg = "black")
canvas.pack(side = "top")



##인생시간 출력
hour = tk.Label(canvas, text = "00", font = ("Digital-7", 100, "bold"), bg = "black", fg = "#39ff14")
hour.place(x = 15, y = 30)

colon = tk.Label(canvas, text = ":", font = ("Digital-7", 100, "bold"), bg = "black", fg = "#39ff14")
colon.place(x = 160, y = 30)

minute = tk.Label(canvas, text = "00", font = ("Digital-7", 100, "bold"), bg = "black", fg = "#39ff14")
minute.place(x = 200, y = 30)

colon = tk.Label(canvas, text = ":", font = ("Digital-7", 100, "bold"), bg = "black", fg = "#39ff14")
colon.place(x = 345, y = 30)

second = tk.Label(canvas, text = "00", font = ("Digital-7", 100, "bold"), bg = "black", fg = "#39ff14")
second.place(x = 385, y = 30)

ampm = tk.Label(canvas, text = "PM", font = ("Digital-7", 50, "bold"), bg = "black", fg = "#39ff14")
ampm.place(x = 520, y = 30)


##현재시간 출력
FrmCurrent = tk.Frame(window, bg = "black")
FrmCurrent.pack(side = "bottom", anchor = 'e', pady = 5)

lblCurrent = tk.Label(FrmCurrent, text = "현재 시간은 ", font = ("Digital-7", 10, "bold"), bg = "black", fg = "white")
lblCurrent.pack(side = "left")

Chour = tk.Label(FrmCurrent, text = "00", font = ("Digital-7", 20, "bold"), bg = "black", fg = "white")
Chour.pack(side = "left")

Ccolon = tk.Label(FrmCurrent, text = ":", font = ("Digital-7", 20, "bold"), bg = "black", fg = "white")
Ccolon.pack(side = "left")

Cminute = tk.Label(FrmCurrent, text = "00", font = ("Digital-7", 20, "bold"), bg = "black", fg = "white")
Cminute.pack(side = "left")

Ccolon = tk.Label(FrmCurrent, text = ":", font = ("Digital-7", 20, "bold"), bg = "black", fg = "white")
Ccolon.pack(side = "left")

Csecond = tk.Label(FrmCurrent, text = "00", font = ("Digital-7", 20, "bold"), bg = "black", fg = "white")
Csecond.pack(side = "left")

Campm = tk.Label(FrmCurrent, text = "PM", font = ("Digital-7", 20, "bold"), bg = "black", fg = "white")
Campm.pack(side = "left")



##루프 돌려서 실행
startTimer()
window.mainloop()







