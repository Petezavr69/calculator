from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
import webbrowser


def OTNIMAEM():

    global text1 
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 - num2
    res = str(res)
    res = '\n'+res
    text1.insert(1.0, res)
    label.config(text=res)   
    
def SLOZHILI():
    
    global text1
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 + num2
    res = str(res)
    res = '\n'+res
    label.config(text=res)
    text1.insert(1.0, res)
    
def PODELILI():
    
    global text1
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    if num2 == 0:
    
        msg = messagebox.showinfo( "err", "can't divide by zero")
    	
    else:
    
        res = num1 / num2
        res = str(res)
        res = '\n'+res
        label.config(text=res)
        text1.insert(1.0, res)
        
def UMNOZILI():
    
    global text1
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    res = num1 * num2
    res = str(res)
    res = '\n'+res
    label.config(text=res)
    text1.insert(1.0, res)

def HEXIM():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())      
    res1 = hex(num1)  
    res2 = hex(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def STEPEN():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res = num1**num2
    res = str(res)
    res = '\n'+res
    label.config(text=res)
    text1.insert(1.0, res)

def KOREN():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = num1**(0.5)
    res2 = num2**(0.5)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def FAKTORIAL():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.factorial(num1)
    res2 = math.factorial(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)    
    text1.insert(1.0, itog)
    
def OCTIM():

    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())      
    res1 = oct(num1)  
    res2 = oct(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)

def BINIM():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())      
    res1 = bin(num1)  
    res2 = bin(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def ANIME_GRIL():
    
    webbrowser.open ('https://www.youtube.com/watch?v=_v3CJ1x_Fto', new=2)
    
def COSINUSB():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.cos(num1)
    res2 = math.cos(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def SINUSB():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.sin(num1)
    res2 = math.sin(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def TANGESB():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.tan(num1)
    res2 = math.tan(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
        
def COTANGENSB():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.tan(num1)
    res2 = math.tan(num2)
    itog = 1/res1,1/res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)    
    text1.insert(1.0, itog)
    
def ARCCOSINUS():

    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.acos(num1)
    res2 = math.acos(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def ARCSINUS():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.asin(num1)
    res2 = math.asin(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def ARCTANGENS():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res1 = math.atan(num1)
    res2 = math.atan(num2)
    itog = res1,res2
    itog = str(itog)
    itog = '\n'+itog
    label.config(text=itog)
    text1.insert(1.0, itog)
    
def ARCCOTANGENS():
    
    global text1
    num1 = int(entry1.get())  
    num2 = int(entry2.get())
    res = math.atan2(num1,num2)
    res = str(res)
    res = '\n'+res
    label.config(text=res)    
    text1.insert(1.0, res)
  
def GET_INPUT():
    global innput
    innput = text2.get("1.0","end-1c")
    
def SAFFE():

    global text2 
    innput = text2.get("1.0","end-1c")
    with open('text.txt','w') as fille:
    	fille.write(innput)
    	
def OPENN():


    global text2
    linnes = []
    output = open('text.txt')
    
    for line in output:
    	linnes.append(line)
    res = ''.join(str(x) for x in linnes)
    text2.insert(1.0, res)
    
    
    
    
            
root = Tk()
root.title("calculator")


w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w=w//2
h=h//2
root.geometry('545x562+{}+{}'.format(w-200,h-200))


label= Label(root, text="")

entry1 = Entry(root, width = 42)
entry1.place(x = 100, y= 58)


entry2 = Entry(root, width = 42)
entry2.place(x = 100, y= 106)


text1 = Text(width=32, height=15, wrap=WORD)
text1.place(x=10,y=250)


text2 = Text(root, width=32, height=15, wrap=WORD)
text2.place(x=275,y=250)


Button(root, text="-", width=6, height=2, command=OTNIMAEM).place(x=10,y=10)

Button(root, text="+", width=6, height=2, command=SLOZHILI).place(x=10,y=58)

Button(root, text="/", width=6, height=2, command=PODELILI).place(x=10,y=106)

Button(root, text=".", width=6, height=2, command=UMNOZILI).place(x=10,y=154)

Button(root, text="^", width=6, height=2, command=STEPEN).place(x=85,y=154)

Button(root, text="sqrt", width=6, height=2, command=KOREN).place(x=160,y=154)

Button(root, text="!", width=6, height=2, command=FAKTORIAL).place(x=235,y=154)

Button(root, text="SIN", width=6, height=2, command=SINUSB).place(x=310,y=154)

Button(root, text="COS", width=6, height=2, command=COSINUSB).place(x=385,y=154)

Button(root, text="HEX", width=6, height=2, command=HEXIM).place(x=10,y=202)

Button(root, text="OCT", width=6, height=2, command=OCTIM).place(x=85,y=202)

Button(root, text="BIN", width=6, height=2, command=BINIM).place(x=160,y=202)

Button(root, text="ANIME", width=6, height=2, command=ANIME_GRIL).place(x=235,y=202)

Button(root, text="CTG", width=6, height=2, command=COTANGENSB).place(x=310,y=202)

Button(root, text="TAN", width=6, height=2, command=TANGESB).place(x=385,y=202)

Button(root, text="ACOS", width=6, height=2, command=ARCCOSINUS).place(x=460,y=154)

Button(root, text="ASIN", width=6, height=2, command=ARCSINUS).place(x=460,y=106)

Button(root, text="ATAN", width=6, height=2, command=ARCTANGENS).place(x=460,y=58)

Button(root, text="ARCTG", width=6, height=2, command=ARCCOTANGENS).place(x=460,y=202)

Button(root, text="OPEN", width=6, height=2, command=OPENN).place(x=276,y=512)

Button(root, text="SAFE", width=6, height=2, command=lambda: SAFFE()).place(x=460,y=512)

label.pack()
root.mainloop()
