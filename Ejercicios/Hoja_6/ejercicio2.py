def calcular_integral(tupla, D):
    integral = 0
    for i in range(len(tupla) - 1):
        integral += (tupla[i] + tupla[i+1]) * D / 2
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