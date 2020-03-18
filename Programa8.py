import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk
# Download comando: python -m pip install ttkthemes

# autor: backup_python.dev


raiz = ThemedTk(theme="equilux")
v = tk.IntVar()
v.set("")
raiz.geometry("265x188")
raiz.resizable(0,0)
raiz.title("Radiobutton")
tipo_de_letra =  "Helvetica 13"

# LABEL 
Etiqueta = ttk.Label(raiz,text="Elige un lenguaje de programación:",
font=tipo_de_letra,width=50).pack()
Etiqueta2 = ttk.Label(raiz,width=50).pack()

lenguajes = ["Python","Java","C#","Kotlin","C++"]
def MostrarEleccion():
    if v.get() == 1:
        print(lenguajes[0])
    elif v.get() == 2:
        print(lenguajes[1])
    elif v.get() == 3:
        print(lenguajes[2])
    elif v.get() == 4:
        print(lenguajes[3])    
    else:
        print(lenguajes[4])        

def RadioButton():
    for item, lenguaje in enumerate(lenguajes):
        item=item+1
        rButton = ttk.Radiobutton(raiz,text=lenguaje,
        variable=v,command=MostrarEleccion,
        value=item,width=100).pack(anchor=tk.W)
    
# BLOQUE PRINCIPAL
RadioButton()

raiz.mainloop()

