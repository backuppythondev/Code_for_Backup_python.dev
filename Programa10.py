import numpy as np
import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib


# autor: backup_python.dev

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(X) 
S = np.sin(X)

plt.style.use('dark_background')
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")

plt.legend(('Función coseno', 'Función seno'),
prop = {'size': 10}, loc='upper left')

plt.yticks(np.linspace(-1, 1, 3, endpoint=True))
plt.xlabel('Tiempo / s',color='orange',fontsize=14)
plt.ylabel('Amplitud / cm',color='green',fontsize=14)
plt.title('REPRESENTACIÓN DE FUNCIONES SENO Y COSENO ',
color='white',fontsize=16)
plt.locator_params(axis="both",tight=True)
plt.show()            