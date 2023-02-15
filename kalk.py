from tkinter import *
from tkinter import ttk
import random



def OTNIMAEM():

    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 - num2
    label.config(text=res)   
    
def SLAZILI():
    
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 + num2
    label.config(text=res)
    
def PODELILI():
    
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    if num2 == 0:
    	label.config(text="can't divide by zero")
    else:
        res = num1 // num2
        label.config(text=res)
    
def UMNOZILI():
    
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 * num2
    label.config(text=res)
    

root = Tk()
root.title("calculator")


w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w=w//2
h=h//2
root.geometry('400x200+{}+{}'.format(w-200,h-200))



label= Label(root, text="")
entry1 = Entry(root, width = 35)
entry1.place(x = 100, y= 55)
entry2 = Entry(root, width = 35)
entry2.place(x = 100, y= 100)

Button(root, text="-", width=6, height=2, command=OTNIMAEM).place(x=10,y=10)

Button(root, text="+", width=6, height=2, command=SLAZILI).place(x=10,y=55)

Button(root, text="/", width=6, height=2, command=PODELILI).place(x=10,y=95)

Button(root, text=".", width=6, height=2, command=UMNOZILI).place(x=10,y=135)

label.pack()
root.mainloop()
