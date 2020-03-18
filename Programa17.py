import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib 


# autor: backup_python.dev

porcentajes = [29,20,17,12,10,7,5]

lenguajes =['PHP','Java','Python',
        'Ruby','C#','JavaScript',
        'Otros']

plt.style.use('fast')
plt.figure(figsize=(9, 6), dpi=80)
plt.pie(porcentajes,autopct='%2.0f%%', shadow=True)
plt.xlabel('FALLOW : @backup_python.dev',fontsize=14)
plt.title('.:: LENGUAJES UTILIZADOS EN BACKEND ::.',
                bbox={'facecolor':'0.8', 'pad':5})

for item in lenguajes:
    plt.legend(lenguajes,title='Lenguajes',prop = {'size': 12}, 
            loc='center left',
            bbox_to_anchor=(1, 0, 0.5, 1))


plt.show()



