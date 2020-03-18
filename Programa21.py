import random as r
import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib


# autor: backup_python.dev
x = []
y = []
for item in range(1,15):
    x.append(r.randint(1,70))
    y.append(r.randint(1,30))

plt.style.use('dark_background')
plt.figure(figsize=(10, 6), dpi=80)
plt.ylim(-1,40)
# Configurar las características del gráfico
plt.scatter(x, y, label = 'DATOS',color = 'blue')
#Definir título y nombres de ejes
plt.title('GRÁFICO DE DISPERSIÓN',
bbox={'facecolor':'0.2', 'pad':10})
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda y figura
plt.legend()
plt.show()