def procesar_tupla(tupla: tuple[str, ...], palabra: str) -> tuple[int, str, str, bool]:
    """
    Función que procesa una tupla de palabras y una palabra suelta, 
    devolviendo la longitud de la tupla, la primera y última palabra 
    de la tupla y si la palabra suelta está contenida en la tupla.
    Args:
        tupla (tuple[str, ...]): Tupla de palabras
        palabra (str): Palabra suelta

    Returns:
        tuple[int, str, str, bool]: Longitud de la tupla, primera y última palabra y 
        si la palabra suelta está contenida
    """
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