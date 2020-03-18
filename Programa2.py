import random as r
# autor: backup_python.dev

def cargar():
    lista = []
    for item in range(20):
        lista.append(r.randint(1,889))
    return lista    

def Reverse(lista):
    lista2=[]
    for item in range(len(lista),0,-1):
        lista2.append(lista[item-1])
    return lista2   



def imprimir(lista):
    print(lista)

def mezclar(lista):
    r.shuffle(lista)

    
lista = cargar()
imprimir(lista)
mezclar(lista)
imprimir(lista)
