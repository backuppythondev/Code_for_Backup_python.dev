import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib 

# autor: backup_python.dev

porcentajes = [29,20,17,12,10,7,5]

lenguajes =['PHP','Java','Python','Ruby','C#',
            'JavaScript','Otros']

plt.style.use('fast')
plt.figure(figsize=(10, 6), dpi=80)
plt.pie(porcentajes,wedgeprops=dict(width=0.5),
 startangle=-50,autopct='%2d%%',labels=lenguajes,shadow=True)
plt.xlabel('FALLOW : @backup_python.dev',fontsize=14)
plt.title('.:: LENGUAJES UTILIZADOS EN BACKEND ::.',
                bbox={'facecolor':'0.8', 'pad':9})

for item in lenguajes:
    plt.legend(lenguajes,title='LENGUAJES',prop = {'size': 14}, 
            loc='center left',
            bbox_to_anchor=(1.1, 0,1.5, 1))


plt.show()

