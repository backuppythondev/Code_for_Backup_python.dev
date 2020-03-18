import matplotlib.pyplot as plt
import random as r
# DOWNLOAD: python -m pip install matplotlib


# autor: backup_python.dev

#datos = [100,94.4,90.2,88.5,83.8,80.3,76.7]
datos =[]
for i in range(1,8):
    datos.append(r.randint(1,100))
lenguajes = ['Python','C++','C','Java',
            'C#','R','Matlab']

colores = ["#EE6055","#60D394","#AAF683",
            "#FFD97D","#8D6372","#4A7B90",
            "#F2D920"]

plt.style.use('dark_background')
plt.figure(figsize=(10, 6), dpi=80)
x = range(len(datos))
plt.bar(x,datos,width=0.8, align='center',color=colores)
plt.xticks(x,lenguajes)
plt.xlabel('FALLOW : @backup_python.dev',fontsize=12,color="white")
plt.title('.:: RANKING LENGUAJES DE PROGRAMACIÓN 2019 ::.',
                bbox={'facecolor':'0.1', 'pad':10})
plt.show()



