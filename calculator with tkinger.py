from tkinter import *
from tkinter import messagebox
import os
from tkinter import PhotoImage


def CalcWin():
    CalcWin = Tk()
    CalcWin.title("Calculator")
    CalcWin.geometry("500x500")
    aeq = "="
    adi = "/"
    amul = "*"
    apl = "+"
    ami = "-"
    a0 = 0
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 4
    a5 = 5
    a6 = 6
    a7 = 7
    a8 = 8
    a9 = 9
    idrk = 0
    global answer
    answer= int()
    answer = 0
    global answerdisplay
    answerdisplay = StringVar(value = "")
    



    def UpdateAns(num):
        
        current = answerdisplay.get()
        answerdisplay.set(str(current) + str(num))
        return(answer)



    def Clear():
        answerdisplay.set("")



    def Calculate():
        idk = eval(answerdisplay.get())
        answerdisplay.set(idk)
        
    answer = Frame(CalcWin)
    answer.pack()
    buttons = Frame(CalcWin)
    buttons.pack()
    
    AnswerLabel=Label(answer, text="answer: ").grid(row=1, column=0)
    
    ShowAns=Entry(answer, textvariable=answerdisplay,width=14).grid(row=1, column=1)
    
    
    n1 = Button(buttons, text="   1   " ,width=5, height=2, command=lambda:UpdateAns(a1)).grid(row=2, column=3)
    
    n1 = Button(buttons, text="   2   ",width=5, height=2, command=lambda:UpdateAns(a2)).grid(row=2, column=4)
    
    n1 = Button(buttons, text="   3   ",width=5, height=2, command=lambda:UpdateAns(a3)).grid(row=2, column=5)
    
    
    n1 = Button(buttons, text="   4   ",width=5, height=2, command=lambda:UpdateAns(a4)).grid(row=3, column=3)
    
    n1 = Button(buttons, text="   5   ",width=5, height=2, command=lambda:UpdateAns(a5)).grid(row=3, column=4)
    
    n1 = Button(buttons, text="   6   ",width=5, height=2, command=lambda:UpdateAns(a6)).grid(row=3, column=5)
    
    
    n1 = Button(buttons, text="   7   ",width=5, height=2, command=lambda:UpdateAns(a7)).grid(row=4, column=3)
    
    n1 = Button(buttons, text="   8   ",width=5, height=2, command=lambda:UpdateAns(a8)).grid(row=4, column=4)
    
    n1 = Button(buttons, text="   9   ",width=5, height=2, command=lambda:UpdateAns(a9)).grid(row=4, column=5)

    n1 = Button(buttons, text="   0   ",width=5, height=2, command=lambda:UpdateAns(a0)).grid(row=5, column=4)



    n1 = Button(buttons, text="   +   ",width=5, height=2, command=lambda:UpdateAns(apl)).grid(row=2, column=6, sticky=W)
    n1 = Button(buttons, text="   -   ",width=5, height=2, command=lambda:UpdateAns(ami)).grid(row=3, column=6, sticky=W)
    n1 = Button(buttons, text="   /   ",width=5, height=2, command=lambda:UpdateAns(adi)).grid(row=4, column=6, sticky=W)
    n1 = Button(buttons, text="   x   ",width=5, height=2, command=lambda:UpdateAns(amul)).grid(row=5, column=6, sticky=W)
    n1 = Button(buttons, text="   =   ",width=5, height=2, command=lambda:Calculate()).grid(row=5, column=5, sticky=W)
    n1 = Button(buttons, text="   C   ",width=5, height=2, command=lambda:Clear()).grid(row=5, column=3, sticky=W)


    
    





CalcWin()
