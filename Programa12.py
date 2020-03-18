import numpy as np
import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib & numpy


theta = np.linspace(0,2*np.pi,1000)
r = 4*np.cos(8*theta)

plt.style.use('Solarize_Light2')
plt.figure(figsize=(10, 6), dpi=90)
plt.subplot(111, projection="polar")
plt.plot(theta,r,color="red",linewidth=2.5)
plt.title("GRÁFICA: ROSA POLAR",
color='blue',fontsize=12)

plt.show()