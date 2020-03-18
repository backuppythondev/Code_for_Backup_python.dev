import tkinter as tk

# autor: backup_python.dev

raiz = tk.Tk()

raiz.title("NEW YEAR")
raiz.geometry("679x189")
raiz.resizable(0,0)
tipoletra = "Helvetica 50"
color="#3A76AA"
raiz.config(background=color)
texto = tk.Label(raiz,text="¡FELIZ AÑO NUEVO!",
font=tipoletra,bg=color,fg="#C23B14")

texto2 = tk.Label(raiz,text="2020",
font=tipoletra,bg=color,fg="#761021")

texto.place(x=10,y=30)
texto2.place(x=250,y=110)

raiz.mainloop()