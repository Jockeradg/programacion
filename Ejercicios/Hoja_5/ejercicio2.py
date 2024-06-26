def indice_valor_mas_cercano(lista:list[float])->int:
    promedio = sum(lista) / len(lista)
    diferencia_minima = abs(lista[0] - promedio)
    indice_minimo = 0

    for i in range(1, len(lista)):
        diferencia_actual = abs(lista[i] - promedio)
        if diferencia_actual < diferencia_minima:
            diferencia_minima = diferencia_actual
            indice_minimo = i

    return indice_minimo

def main():
    lista = [1.5, 2.7, 3.9, 4.2, 5.1, 6.8, 7.3, 8.6, 9.4, 10.0]
    indice = indice_valor_mas_cercano(lista)
    print("El índice del valor más cercano al promedio es:", indice)

main()