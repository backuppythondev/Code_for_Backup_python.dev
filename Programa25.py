from translate import Translator
# DOWNLOAD: python -m pip install translate


# autor: backup_python.dev

def Traductor():
    texto_original = input("Ingrese texto: ")
    traductor = Translator(from_lang="Spanish",to_lang="English")
    traduccion = traductor.translate(texto_original)
    return traduccion



# BLOQUE PRINCIPAL 

traductor = Traductor()
print(traductor)


class name:
    name=True
    def arrancar(self,name):
        self.name=name



