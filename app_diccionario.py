def buscar_palabra(palabra)
    palabra_limpia = palabra.lower()
    if palabra_limpia in diccionario_local: # lo dejo así por ahora
        return diccionario_local[palabra_limpia]
    else:
        return None
    
def mostrar_resumen(datos):
    palabra = datos.get("word","")
    print("Análisis de la palabra: {palabra.upper()}")

    if(datos.get("phonetics")):
        print("Contiene pronunciación y transcripción")
    else:
        print("No se tienen datos sobre la pronunciación")

    if(datos.get("meanings")):
        print("Contiene definiciones")
    else:
        print("No hay definiciones")

def mostrar_palabra_completa(datos):
    palabra = datos.get("word", "")
    print("Datos completos de: {palabra.upper()}")

    