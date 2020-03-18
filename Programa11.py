import numpy as np
import matplotlib.pyplot as plt


# autor: backup_python.dev

theta = np.linspace(0,2*np.pi)
r = 5 + 50*theta

plt.style.use('Solarize_Light2')
plt.figure(figsize=(10, 6), dpi=90)


#theta = np.linspace(0,2*np.pi,1000)
#r = 4**2*np.sin(2*theta)

plt.subplot(111, projection="polar")
plt.plot(theta,r,color="red")
plt.title("GRÁFICAS EN COORDENADAS POLARES",
color='blue',fontsize=12)

plt.show()