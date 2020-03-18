import matplotlib.pyplot as plt
# DOWNLOAD: python -m pip install matplotlib 

# autor: backup_python.dev

y = [10,20,15,20,15,20]
plt.style.use('fast')
plt.figure(figsize=(10, 5), dpi=80)
plt.pie(y)
plt.xlabel('FALLOW : @backup_python.dev',fontsize=14)
plt.title('GRÁFICO CIRCULAR')
plt.legend( ('10 %','20 %','15 %',
            '20 %','15 %','20 %'),
            prop = {'size': 12}, 
            loc='center left',
            bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()