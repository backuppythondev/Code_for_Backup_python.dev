
# autor: backup_python.dev

def TablaMult(i,n):
    if n>0:
        TablaMult(i,n-1)
    print("{:2d} {:^3s} {:2d} {:^3s}{:3d}"
    .format(i,"x",n,"=",i*n))        

# BLOQUE PRINCIPAL
TablaMult(8,12)



def TablaMult(n):
    if n>0:
        TablaMult(n-1)
    print("{:2d} {:^3s} {:2d} {:^3s}{:3d}"
    .format(n,"x",n,"=",n*n)) 

# BLOQUE PRINCIPAL
TablaMult(12)



