import math
from typing import Final

DELTA: Final[float] = 0.1

def calcular_integral(tupla:tuple[float,...])->float:
    """
    Calcula la integral definida de una lista de números reales. La integral se calcula mediante la regla del trapecio.


    Args:
        tupla (tuple[float,...]): Tupla de números reales. Contiene números reales.

    Returns:
        float: La integral definida de la lista de números reales.
    """
    integral: float = 0
    for i in range(len(tupla) - 1):
        integral += (tupla[i] + tupla[i+1]) * DELTA / 2
    return integral

def main():
    # Generar una lista de al menos 100 números reales
    lista = [i * 0.1 for i in range(100)]

    # Calcular la integral definida de la lista
    integral = calcular_integral(lista, 0.1)

    # Imprimir el resultado
    print("La integral definida es:", integral)

if __name__ == "__main__":
    main()