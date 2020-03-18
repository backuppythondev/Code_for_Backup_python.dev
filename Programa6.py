# autor: backup_python.dev
import  random as r
lista=[]
def Generar():
    n = int(input("Ingrese tamaño de la lista: "))
    for i in range(0,n):
        lista.append(r.randint(1,100))   
    return n
def BusquedaRecursiva(lista,n,dato):
    if n==0 and lista[n]==dato:
        return True
    elif n==0:
        return False
    elif lista[n]==dato:
        return True     
    else:
        return BusquedaRecursiva(lista,n-1,dato)

# BLOQUE PRINCIPAL
n = Generar() 
Busqueda = BusquedaRecursiva(lista,n-1,18)
print(lista)
print(Busqueda)
