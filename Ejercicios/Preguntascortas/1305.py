try:
    with open("entrada.txt", "r") as file:
        number = float(file.read())
        print("Número leído:", number)
except IOError:
    print("Error al leer el archivo.")