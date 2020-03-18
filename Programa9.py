import numpy as np
import matplotlib.pyplot as plt
#DOWNLOAD: python -m pip install matplotlib


# autor: backup_python.dev

# HOJAS DE ESTILO
plt.style.use('Solarize_Light2')

x = np.linspace(0, 8*np.pi,800) 

def FuncionSen(x):
    y = np.sin(x)
    return y

# BLOQUE PRINCIPAL
y = FuncionSen(x)

# GRAFICAR
plt.axhline(y=0,color='black',lw="1")
plt.plot(x,y,'--r',lw="2")
plt.yticks(np.linspace(-1, 1, 2, endpoint=True))
plt.xlabel('Tiempo / s',color='blue')
plt.ylabel('Amplitud / cm',color='green')
plt.title('REPRESENTACION DE UNA FUNCION SENO ',color='orange')

plt.show()