import math

def pinta_linea(x_1: int, y_1: int, x_2: int, y_2: int):
    print(f"Línea entre ({x_1}, {y_1}) y ({x_2}, {y_2})")

def pinta_triangulo(a: float, b: float, alpha: float):
    """
    Funcion que dibuja un triángulo con los lados a y b y el ángulo alpha.
    Args:
        a (float): longitud del lado a, en pixel
        b (float): longitud del lado b, en pixel
        alpha (float): ángulo alpha, en radianes
    """
    # Convert alpha from radians to degrees
    alpha_deg = math.degrees(alpha)
    
    # Calculate the coordinates of the vertices A, B, and C
    x_a:int = round(b * math.cos(alpha))
    y_a:int = round(b * math.sin(alpha))
    
    x_b:int = round(a)
    y_b:int = 0
    
    x_c:int = 0
    y_c:int = 0
    
    # Draw the triangle by calling pinta_linea() for each side
    pinta_linea(x_a, y_a, x_b, y_b)
    pinta_linea(x_b, y_b, x_c, y_c)
    pinta_linea(x_c, y_c, x_a, y_a)

# Test the pinta_triangulo() function
pinta_triangulo(3.5, 4.2, math.radians(45))