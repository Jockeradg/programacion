from fundamentos.dibujo import Dibujo, Imagen

def main():
    """
    Función principal que ejecuta la simulación de un dron volando y luego 
    chocando.

    La función crea una ventana de dibujo y muestra una imagen de un edificio y
    un dron.
    Luego, mueve el dron hacia arriba y hacia la derecha para simular un vuelo 
    y un choque.
    Finalmente, muestra una imagen de explosión y espera a que el usuario 
    cierre la ventana.

    Args:
        None

    Returns:
        None
    """
    # Crear la ventana
    lienzo = Dibujo("Título", 900, 800)
    
    # Crear una imagen para el edificio
    building = Imagen(lienzo, 700, 500, "edificio.png")
    
    # Crear una imagen para el dron
    dron = Imagen(lienzo, 500, 800, "dron.png")
    
    # Mover el dron hacia arriba
    for _ in range(200):
        dron.mueve(0, -2)
        lienzo.pinta()
    
    # Mover el dron hacia la derecha y simular un choque
    for _ in range(50):
        dron.mueve(2, 0)
        lienzo.pinta()
    
    # Simular una explosión
    explosion = Imagen(lienzo, 600, 400, "boom.png")
    
    # Esperar a que se cierre la ventana y destruirla
    lienzo.espera()
    lienzo.destruye()

if __name__ == "__main__":
    main()