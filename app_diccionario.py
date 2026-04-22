import httpx

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

def buscar_palabra(palabra_buscada):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra_buscada}"

    try:
        respuesta = httpx.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            info = datos[0]

            # Fonética
            transcripcion = "/.../"
            audio = "Sin audio"
            for phon in info.get("phonetics", []):
                if phon.get("text"): transcripcion = phon.get("text")
                if phon.get("audio"): audio = phon.get("audio")
            fonetica_obj = Fonetica(transcripcion, audio)
            # Significados y Definiciones
            lista_significados = []
            for mean in info.get("meanings", []):
                categoria = mean.get("partOfSpeech", "Desconocido")
                lista_definiciones = []
                for dfn in mean.get("definitions", []):
                    texto_def = dfn.get("definition", "")
                    sinonimos = dfn.get("synonimyms", "")
                    lista_definiciones.append(Definicion(texto_def, sinonimos))
                lista_significados.append(Significado(categoria, lista_definiciones))
            
            return Palabra(palabra_buscada, lista_significados, fonetica_obj)
        else:
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")

while True:
    palabra_input = input("\nEscribe una palabra en inglés (o 'salir' para terminar): ").strip()
    if palabra_input.lower() == 'salir':
        print("Fin del programa")
        break
    if palabra_input == "":
        print("Error: introduzca una palabra válida.")
        continue

    resultado = buscar_palabra(palabra_input)
    if resultado is not None:
        while True:
            print("\nSelecciona qué información quieres ver en detalle:")
            print("1. Mostrar todo")
            print("2. Solo la pronunciación")
            print("3. Solo los significados")
            print("4. Volver a buscar otra palabra")
            opcion = input("Elige una opción (1/2/3/4): ").strip()
            if opcion == "1":
                print(f"\n Análisis completo de la palabra {resultado.texto.upper()}")
                print(f"Pronunciación: {resultado.fonetica.transcripcion} (Audio: {resultado.fonetica.audio_url})")
                print("Significados:")
                for sig in resultado.significados:
                    print(f"[{sig.categoria.upper()}]")
                    for i, definicion in enumerate(sig.definiciones, 1):
                        print(f"    {i}. {definicion.texto}")
            elif opcion == "2":
                print(f"\n Pronunciación")
                print(f"Transcripción fonética: {resultado.fonetica.transcripcion}")
                print(f"Enlace de audio: {resultado.fonetica.audio_url}")
            elif opcion == "3":
                print(f"\n Significados:")
                for sig in resultado.significados:
                    print(f"  [{sig.categoria.upper()}]")
                    for i, definicion in enumerate(sig.definiciones, 1):
                        print(f"{i}. {definicion.texto}")
            elif opcion == "4":
                break
            else:
                print("Error: Opción no válida. Por favor, elige 1, 2, 3 o 4.")
    else:
        print(f"Error: No se encontró la palabra '{palabra_input}' en el diccionario.")
 