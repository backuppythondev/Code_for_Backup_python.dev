import PIL.ImageFilter as im
import PIL.Image as image

# autor: backup_python.dev

imagen = image.open("pythondev.png")

# Usar el filtro de nuestro agrado
filtro_imagen = imagen.filter(im.BLUR)

# Guardar imagen con la extensión de tu agrado
filtro_imagen.save("imagenpython.png")

# Abrir imagen
filtro_imagen.show()
