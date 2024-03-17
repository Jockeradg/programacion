def obtener_primera_palabra(texto:str)->str:
    """
    Función que devuelve la primera palabra de un texto. Ademas hace distintas
    transformaciones al texto, sin modificar el original.
    Args:
        texto (str): Frase cualquiera

    Returns:
        str: Primera palabra del texto
    """
    # Paso a)
    primer_punto:int = texto.find('.')
    
    # Paso b)
    texto_sin_primera_frase:str = texto[primer_punto+1:]
    
    # Paso c)
    texto_sin_espacios:str = texto_sin_primera_frase.strip()
    
    # Paso d)
    primer_espacio:int = texto_sin_espacios.find(' ')
    
    # Paso e)
    primera_palabra:str = texto_sin_espacios[:primer_espacio]
    
    return primera_palabra