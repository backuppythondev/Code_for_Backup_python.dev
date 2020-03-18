import tkinter as tk
import pyqrcode as qrcode
from tkinter import ttk 
from PIL import Image, ImageTk

# autor: backup_python.dev

raiz = tk.Tk()

raiz.title("Fallow: backup_python.dev")
raiz.geometry("440x480")
raiz.iconbitmap('python.ico')
# Design
image = Image.open("color.jpg")
photo = ImageTk.PhotoImage(image)
x = tk.Label (image = photo)
x.pack()

raiz.resizable(0,0)

tipoletra = "Helvetica 12"
label = ttk.Label(raiz,text="Url :",
font=tipoletra)

var1 = tk.StringVar()

liga = ttk.Entry(raiz,textvariable=var1,justify="center",
width= 40,font=tipoletra)


def GenerarQr(Event):
    global dato
    url = var1.get()
    try:
        url = qrcode.create(url)
        dato = url.xbm(scale=7)
        global img_bit
        img_bit  = tk.BitmapImage(data=dato,foreground="white",background="#244F7F")
        label2.config(image=img_bit)
    except:
        pass

def limpiar():
    var1.set("")


BtnLimpiar = ttk.Button(raiz,text="Limpiar",
width=14,command=limpiar)
liga.bind("<KeyPress>",GenerarQr)

label2=tk.Label(raiz)
label2.place(x=70,y=127)

label.place(x=17,y=30)
liga.place(x=57,y=30)
BtnLimpiar.place(x=170,y=70) 

raiz.mainloop()