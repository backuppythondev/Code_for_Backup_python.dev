import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk
from translate import Translator
# DOWNLOAD: python -m pip install translate 

# autor: backup_python.dev

raiz = ThemedTk(theme="vista")
raiz.geometry("600x300")
raiz.title("Traductor")
letra = "Helvetica 12 bold"

# StringVar
var = tk.StringVar()
var2 = tk.StringVar()

text  = ttk.Label(raiz,text="Español:",font=letra)
text2  = ttk.Label(raiz,text="Inglés:",font=letra)
texto = ttk.Entry(raiz,textvariable=var2,font=letra,width=70)
traduccion = ttk.Entry(raiz,textvariable=var,font=letra,width=70)

def Traductor():
    traductor = Translator(from_lang="Spanish",to_lang="English")
    traduccion = traductor.translate(texto.get())
    return var.set(traduccion)

BtnT = ttk.Button(raiz,text="Traducir",width=14,command=Traductor)

BtnT.place(x=50,y=190)       
text.place(x=10,y=10)
text2.place(x=10,y=100)
texto.place(x=87,y=10)
traduccion.place(x=88,y=100)
raiz.mainloop()