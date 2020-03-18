from pygame import mixer
import os
#python -m pip install pygame

# autor: backup_python.dev

lista_de_songs = []
index = 0 

# Abrir archivo
directorio = "C:/Users/DELL/Music/Deezer Music"
os.chdir(directorio)
lista_directorio = os.listdir(directorio)

for archivos in lista_directorio:
    if archivos.endswith(".mp3"):
        lista_de_songs.append(archivos)

mixer.init()

mixer.music.load(lista_de_songs[0])
mixer.music.set_volume(30)
mixer.music.play()


while True:
    mensaje = lista_de_songs[index]
    print("\x1b[1;33m"+"")    
    print("##################################################################")
    print("# presione :                                                     #")
    print("# 'p' Pausar                                                     #")
    print("# 'r' Reanudar                                                   #")
    print("# 'a' Anterior                                                   #")
    print("# 's' Siguiente                                                  #")
    print("#   Seleccionar pista: 'l '                                      #")
    print("# 'e' Salir                                                      #")                
    print("##################################################################")
    print("\033[;36m"+"En reproducción: ",mensaje[0:len(mensaje)-4]) 
    control = input("\033[;31m"+"ingrese comando --->   ")

    if control == 'p' or control == 'P':
        mixer.music.pause()
    elif control == 'r' or control == 'R':
        mixer.music.unpause()
    elif control == 'a' or control == 'A':
        index -= 1
        mixer.music.load(lista_de_songs[index])
        mixer.music.play()
    elif control == 's' or control == 'S':
        index += 1
        if index <= len(lista_de_songs)-1:
            mixer.music.load(lista_de_songs[index])
            mixer.music.play() 
        else:
            index=0
            mixer.music.load(lista_de_songs[index])
            mixer.music.play() 

    elif control == 'l' or control =='L':
        print("################### PLATLIST #########################################")
        for item in range(1,len(lista_de_songs)):
            print("\033[;32m"+"",item," ",lista_de_songs[item])
        print("#######################################################################") 
        
        try:        
            pista = int(input("\033[;35m"+"Selecionar pista: "))
        
            if pista <= len(lista_de_songs):
                mixer.music.load(lista_de_songs[pista])
                mixer.music.play() 
                index=pista
        except:
            print("Error")

    else:
        mixer.music.stop()
        break
 

