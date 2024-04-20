def obtener_personas_con_comida_favorita(nombres, comidas, favorita):
    personas_con_favorita = [nombre for nombre, comida in zip(nombres, comidas) if comida == favorita]
    return personas_con_favorita

def main():
    nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]
    comidas = ["Pizza", "Sushi", "Hamburguesa", "Pizza", "Ensalada"]
    favorita = "Pizza"

    personas_con_favorita = obtener_personas_con_comida_favorita(nombres, comidas, favorita)
    print("Personas con comida favorita:", personas_con_favorita)

if __name__ == "__main__":
    main()