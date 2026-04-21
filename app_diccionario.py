class Definicion:
    def __init__(self, texto, sinonimos):
        self.texto = texto
        self.sinonimos = sinonimos # lista?

class Significado:
    def __init__(self, categoria_gramatical, definiciones):
        self.categoria = categoria_gramatical
        self.definiciones = definiciones

class Fonetica:
    def __init__(self, transcripcion, audio_url):
        self.transcripcion = transcripcion
        self.audio_url = audio_url

class Palabra:
    def __init__(self, texto, significados, fonetica):
        self.texto = texto
        self.significados = significados
        self.fonetica = fonetica

# veo que la palabra tenga los datos necesarios
def tiene_informacion_completa(self):
    return self.fonetica is not None and len(self.significados) > 0

while True:
    palabra_input = input("Escribe una palabra en inglés para buscar (o escribe 'salir' para terminar):")
    if palabra_input.lower().strip() == 'salir':
        print("Fin del programa")
        break
    if palabra_input.strip() == "":
        print("Error: introduzca una palabra válida")
        continue
