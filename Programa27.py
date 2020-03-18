import PIL.ImageFilter as im
import PIL.Image as image


# autor: backup_python.dev 

imagen = image.open("pythondev.png")

convertir_imagen = imagen.filter(im.EDGE_ENHANCE_MORE)

convertir_imagen.save("imagenpythonBN.png")

convertir_imagen.show()