from fundamentos.dibujo import Dibujo, Imagen, Linea

def main():
    """
    Función principal que ejecuta la simulación de dos aviones volando y luego 
    chocando.

    La función crea una ventana de dibujo y muestra una imagen de un edificio 
    y dos aviones.
    Luego, mueve los aviones hacia arriba y hacia la derecha para simular un 
    vuelo y un choque.
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
    
    #Definimos las posiciones iniciales del avión de papel
    px:float = 500
    py:float = 700
    lon:float = 30
    anch:float = 30
    
    # Crear una imagen para el dron
    linea_1 = Linea(lienzo, px-lon, py-anch//2,px-(lon*3)//4, py, "red")
    linea_2 = Linea(lienzo, px-(lon*3)//4, py, px-lon, py+anch//2, "red")
    linea_3 = Linea(lienzo, px-lon, py+anch//2, px, py, "red")
    linea_4 = Linea(lienzo, px, py, px-lon, py-anch//2, "red")
    
    #Definimos las posiciones iniciales del avión de papel 2
    px:float = 400
    py:float = 700
    lon:float = 30
    anch:float = 30
    
    # Crear una imagen para el avion 2
    linea_5 = Linea(lienzo, px-lon, py-anch//2,px-(lon*3)//4, py, "red")
    linea_6 = Linea(lienzo, px-(lon*3)//4, py, px-lon, py+anch//2, "red")
    linea_7 = Linea(lienzo, px-lon, py+anch//2, px, py, "red")
    linea_8 = Linea(lienzo, px, py, px-lon, py-anch//2, "red")
    
    # Mover los aviones hacia arriba
    for _ in range(200):
        linea_1.mueve(0, -2)
        linea_2.mueve(0, -2)
        linea_3.mueve(0, -2)
        linea_4.mueve(0, -2)
        linea_5.mueve(0, -2.8)
        linea_6.mueve(0, -2.8)
        linea_7.mueve(0, -2.8)
        linea_8.mueve(0, -2.8)
        lienzo.pinta()
    
    # Mover los aviones hacia la derecha y simular un choque y aterrizaje
    for _ in range(50):
        linea_1.mueve(2, 0)
        linea_2.mueve(2, 0)
        linea_3.mueve(2, 0)
        linea_4.mueve(2, 0)
        linea_5.mueve(6.5, 0)
        linea_6.mueve(6.5, 0)
        linea_7.mueve(6.5, 0)
        linea_8.mueve(6.5, 0)
        lienzo.pinta()
    
    # Simular una explosión
    explosion = Imagen(lienzo, 600, 300, "boom.png")
    
    # Esperar a que se cierre la ventana y destruirla
    lienzo.espera()
    lienzo.destruye()

if __name__ == "__main__":
    main()