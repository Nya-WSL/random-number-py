import os
import random
from tkinter import *
import tkinter.messagebox as tkmb
from tkinter.filedialog import askopenfilename, askopenfilenames, askdirectory, asksaveasfilename

version = "2.0.1"

def clicked():
    global listbox
    global sc
    global lb
    global Compare
    NumberList = ""
    NumberText = int(Number.get())
    RangeMinNumber = int(RangeMin.get())
    RangeMaxNumber = int(RangeMax.get())
    RangeMax1 = int(RangeMaxNumber) + int(1)
    Compare = RangeMax1 - RangeMinNumber
    print(f"最大值：{RangeMaxNumber} 最小值：{RangeMinNumber} 差异：{Compare}") # debug
    if int(NumberText) > int(Compare):
        CompareError()
    if CheckVar.get() == 1:
        NumberList = [random.randint(int(RangeMinNumber),int(RangeMax1)) for _ in range(int(NumberText))]
    elif CheckVar.get() == 0:
        NumberList = random.sample(range(int(RangeMinNumber),int(RangeMax1)),int(NumberText))
    lb = Label(window)
    lb.pack(side=LEFT)
    lb.configure(text = "结果：")
    sc = Scrollbar(window)
    sc.pack(side=LEFT, fill=Y)
    listbox = Listbox(window, selectmode=EXTENDED, yscrollcommand=sc.set, height=5, width=10, borderwidth=0)
    for i in NumberList:
        listbox.insert(END, i)
    listbox.pack(side=LEFT, fill=BOTH)
    sc.config(command=listbox.yview)

def randomStr():
    window.destroy()
    WindowRandomStr = Tk()
    if os.path.exists("Nya-WSL.ico"):
        WindowRandomStr.iconbitmap("Nya-WSL.ico")
    WindowRandomStr.title(f"简易随机字符串生成器v{version} by.Nya-WSL")
    WindowRandomStr.geometry('500x410')
    
    LblNumberCHoice = Label(WindowRandomStr,text = "请输入生成数量")
    LblCsvChoice = Label(WindowRandomStr,text = "请选择需要抽取的csv")
    NumberChoice = Entry(WindowRandomStr,width=10)
    
    btnCsvChoice = Button(WindowRandomStr,fg="black",bg="white",text="选择文件",command=opencsv)
    
    
    LblNumberCHoice.pack()
    NumberChoice.pack()
    LblCsvChoice.pack()
    btnCsvChoice.pack()
    
    
    
    window.mainloop()

def opencsv():
    askopenfilename(title="请选择需要抽取的文件", initialdir=os.getcwd(), filetypes=[("CSV file",'*.csv')])

def reset():
    listbox.destroy()
    sc.destroy()
    lb.destroy()

def CompareError():
    tkmb.showwarning(title="警告", message="输入的生成数量大于最大值 " + str(Compare) + " ！")

def get_var():
    print(CheckVar.get())

def mainWindow():
    global window
    global Number
    global CheckVar
    global RangeMax
    global RangeMin
    window = Tk()
    if os.path.exists("Nya-WSL.ico"):
        window.iconbitmap("Nya-WSL.ico")
    window.title(f"简易随机数生成器v{version} by.Nya-WSL")
    window.geometry('500x410')

    LblNumberCHoice = Label(window,text = "请输入生成数量")
    LblRangeChoiceMin = Label(window,text = "请输入生成范围的最小值")
    LblRangeChoiceMax = Label(window,text = "请输入生成范围的最大值")
    Number = Entry(window,width=10)
    RangeMin = Entry(window,width=10)
    RangeMax = Entry(window,width=10)

    LblNumberCHoice.pack()
    Number.pack()
    LblRangeChoiceMin.pack()
    RangeMin.pack()
    LblRangeChoiceMax.pack()
    RangeMax.pack()

    CheckVar = IntVar()
    CV = Checkbutton(window, text="允许生成重复的值", variable=CheckVar, onvalue=1, offvalue=0, height=1, command=get_var)
    CV.pack()

    btnStart = Button(window,fg="black",bg="white",text="开始",command=clicked)
    btnStart.pack()
    btnRestart = Button(window,fg="black",bg="white",text="重置结果",command=reset)
    btnRestart.pack(pady=5)
    btnRandomStr = Button(window,fg="black",bg="white",text="随机字符串",command=randomStr)
    btnRandomStr.pack()

    window.mainloop()

mainWindow()