import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk


raiz = ThemedTk(theme="equilux")
raiz.title("Mi primer Interfaz")
raiz.geometry("280x260") 
raiz.resizable(0,0)
letra = "Helvetica 12 bold"
raiz.config(bg="black")
# Label
dato1 = ttk.Label(raiz,text="Numero 1 ",font=letra)
dato2 = ttk.Label(raiz,text="Numero 2 ",font=letra)
resultado = ttk.Label(raiz,text="Resultado ",font=letra)
# StringVar
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
# Entry
campo_texto1 = ttk.Entry(raiz,textvariable=var1,justify="center",width= 14,font=letra)
campo_texto2 = ttk.Entry(raiz,textvariable=var2,justify="center",width= 14,font=letra)
campo_texto3 = ttk.Entry(raiz,textvariable=var3,justify="center",width=14,font=letra)

# Place
dato1.place(x=10,y=30)
dato2.place(x=10,y=80)
resultado.place(x=10,y=130)
campo_texto1.place(x=120,y=30)
campo_texto2.place(x=120,y=80)
campo_texto3.place(x=120,y=130)
# Proceso
def Calcular():
    n1 = int(var1.get())
    n2 = int(var2.get()) 
    r  = n1+n2
    return var3.set(r)

# Button
BtnCalcular = ttk.Button(raiz,text="Sumar",width=14,command=Calcular)
BtnCalcular.place(x=100,y=190)    
raiz.mainloop()