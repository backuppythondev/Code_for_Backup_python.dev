import numpy as np
import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib & numpy

t = np.linspace(0, 2*np.pi, 100)
x = 3*np.sin(t)/(1+np.cos(t)**2)
y = 3*np.sin(t)*np.cos(t)/(1+np.cos(t)**2)

plt.style.use('dark_background')
plt.figure(figsize=(10, 6), dpi=80)
plt.plot(x,y,'--r',linewidth=2.5)
plt.title("GRÁFICA: LEMNISCATA",
color='white',fontsize=18)

plt.show()
