import cmath

def ecuaciones(a:float, b:float, c:float)->tuple:
    """
    Calcula las raíces de una ecuación cuadrática.

    Args:
        a (float): Primer termino de la ecuación cuadrática.
        b (float): Segundo termino de la ecuación cuadrática.
        c (float): Tercer termino de la ecuación cuadrática.

    Returns:
        tuple: Devuelve en forma de tupla las soluciones
    """
    discriminante = b ** 2 - (4 * a * c)
    sol_1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    sol_2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    return sol_1, sol_2