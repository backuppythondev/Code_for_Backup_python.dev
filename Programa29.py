import PIL.ImageFilter as img
import PIL.Image as image


# autor: backup_python.dev

imagen = image.open("IglesiaSantoDomingo.jpg")

# Aplicar efecto BLUR
filtro_imagen = imagen.filter(img.BoxBlur(radius=5))

# Guardar imagen con la extensión de tu agrado
filtro_imagen.save("Iglesia_Santo_Domingo.png")

# Abrir imagen
filtro_imagen.show()