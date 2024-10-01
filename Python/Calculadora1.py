#Calculadora
import math
from tkinter import *

root = Tk()
root.title("Calculadora")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def BotonAdd(Numero):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(Numero))

def BotonClr():
    e.delete(0, END)

def Suma():
    global math
    math="suma"
    PrimerNumero = e.get()
    global PNum 
    PNum = int(PrimerNumero)
    e.delete(0, END)

def Resta():
    global math
    math="resta"
    PrimerNumero = e.get()
    global PNum 
    PNum = int(PrimerNumero)
    e.delete(0, END)

def Mult():
    global math
    math="mult"
    PrimerNumero = e.get()
    global PNum 
    PNum = int(PrimerNumero)
    e.delete(0, END)

def Div():
    global math
    math="div"
    PrimerNumero = e.get()
    global PNum 
    PNum = int(PrimerNumero)
    e.delete(0, END)

def Igual():
    match(math):
        case 'suma':
            SNum = e.get()
            e.delete(0, END)
            e.insert(0, PNum + int(SNum))
        case "resta":
            SNum = e.get()
            e.delete(0, END)
            e.insert(0, PNum - int(SNum))
        case 'mult':
            SNum = e.get()
            e.delete(0, END)
            e.insert(0, PNum * int(SNum))
        case 'div':
            SNum = e.get()
            e.delete(0, END)
            e.insert(0, PNum / int(SNum))

boton1 = Button(root, text="1", padx=40, pady=20, command=lambda: BotonAdd(1))
boton2 = Button(root, text="2", padx=40, pady=20, command=lambda: BotonAdd(2))
boton3 = Button(root, text="3", padx=40, pady=20, command=lambda: BotonAdd(3))
boton4 = Button(root, text="4", padx=40, pady=20, command=lambda: BotonAdd(4))
boton5 = Button(root, text="5", padx=40, pady=20, command=lambda: BotonAdd(5))
boton6 = Button(root, text="6", padx=40, pady=20, command=lambda: BotonAdd(6))
boton7 = Button(root, text="7", padx=40, pady=20, command=lambda: BotonAdd(7))
boton8 = Button(root, text="8", padx=40, pady=20, command=lambda: BotonAdd(8))
boton9 = Button(root, text="9", padx=40, pady=20, command=lambda: BotonAdd(9))
boton0 = Button(root, text="0", padx=40, pady=20, command=lambda: BotonAdd(0))

botonSuma = Button(root, text="+", padx=39, pady=20, command=Suma)
botonResta = Button(root, text="-", padx=41, pady=20, command=Resta)
botonMult = Button(root, text="*", padx=41, pady=20, command=Mult)
botondiv = Button(root, text="/", padx=41, pady=20, command=Div)
botonIgual = Button(root, text="=", padx=91, pady=20, command=Igual)
botonBorrar = Button(root, text="clr", padx=86, pady=20, command=BotonClr)

boton1.grid(row=3, column=0)
boton2.grid(row=3, column=1)
boton3.grid(row=3, column=2)

boton4.grid(row=2, column=0)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)

boton7.grid(row=1, column=0)
boton8.grid(row=1, column=1)
boton9.grid(row=1, column=2)

boton0.grid(row=4, column=0)
botonBorrar.grid(row=4, column=1, columnspan=2)
botonSuma.grid(row=5, column=0)
botonIgual.grid(row=5, column=1, columnspan=2)

botonResta.grid(row=6, column=0)
botonMult.grid(row=6, column=1)
botondiv.grid(row=6, column=2)

root.mainloop()