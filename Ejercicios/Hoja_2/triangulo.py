import math

def pinta_linea(x_1: int, y_1: int, x_2: int, y_2: int):
    print(f"Línea entre ({x_1}, {y_1}) y ({x_2}, {y_2})")

def pinta_triangulo(a: float, b: float, alpha: float):
    # Convert alpha from radians to degrees
    alpha_deg = math.degrees(alpha)
    
    # Calculate the coordinates of the vertices A, B, and C
    x_a = 0
    y_a = 0
    
    x_b = round(a)
    y_b = 0
    
    x_c = round(a + b * math.cos(alpha))
    y_c = round(b * math.sin(alpha))
    
    # Draw the triangle by calling pinta_linea() for each side
    pinta_linea(x_a, y_a, x_b, y_b)
    pinta_linea(x_b, y_b, x_c, y_c)
    pinta_linea(x_c, y_c, x_a, y_a)

# Test the pinta_triangulo() function
pinta_triangulo(3.5, 4.2, math.radians(45))