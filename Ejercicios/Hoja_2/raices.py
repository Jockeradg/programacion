import cmath

def ecuaciones(a, b, c):
    discriminante = (b ** 2) - (4 * a * c)
    sol_1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    sol_2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    return sol_1, sol_2