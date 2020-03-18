import numpy as np

import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib & numpy


# autor: backup_python.dev

x  = np.linspace(-2*np.pi, 2*np.pi ,1000)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)+3*np.cos(x)

plt.style.use('dark_background')
plt.figure(figsize=(10, 6), dpi=80)
plt.plot(x,y1,color="red",linewidth=2.5)
plt.plot(x,y2,color="blue",linewidth=2.5)
plt.plot(x,y3,color="white",linewidth=2.5)
plt.ylim(-4,5)
plt.legend(('Función seno', 'Función coseno',
'Función seno(x)+3coseno(x)'),
prop = {'size': 10}, loc='upper right')
plt.title("FUNCIONES",
color='white',fontsize=18)

plt.show()