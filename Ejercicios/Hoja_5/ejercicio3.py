def filtrar_lista(lista, valor_max):
    lista_filtrada = [num for num in lista if num >= 0 and num <= valor_max]
    return lista_filtrada

def main():
    lista_original = [-5, 10, 15, 3, -2, 7]
    valor_max = 10
    lista_filtrada = filtrar_lista(lista_original, valor_max)
    print("Lista original:", lista_original)
    print("Lista filtrada:", lista_filtrada)

if __name__ == "__main__":
    main()