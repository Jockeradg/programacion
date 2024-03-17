def procesar_tupla(tupla: tuple[str, ...], palabra: str) -> tuple[int, str, str, bool]:
    num_palabras = len(tupla)
    primera_palabra = tupla[0]
    ultima_palabra = tupla[-1]
    palabra_contenida = palabra in tupla
    
    return num_palabras, primera_palabra, ultima_palabra, palabra_contenida

def main():
    tupla = ("Hola", "Mundo", "Python", "Programación")
    palabra_suelta = "Python"
    
    resultado = procesar_tupla(tupla, palabra_suelta)
    
    num_palabras, primera_palabra, ultima_palabra, palabra_contenida = resultado
    
    print("Número de palabras:", num_palabras)
    print("Primera palabra:", primera_palabra)
    print("Última palabra:", ultima_palabra)
    print("¿Palabra suelta contenida?:", palabra_contenida)

if __name__ == "__main__":
    main()