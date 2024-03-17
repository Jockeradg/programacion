def main():
    # Crear una lista con los nombres de los planetas del sistema solar
    planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]

    # Mostrar la longitud de la lista
    print("Longitud de la lista:", len(planetas))

    # Crear una sublista con los planetas rocosos
    planetas_rocosos = planetas[:4]

    # Cambiar los nombres de los planetas gaseosos a mayúsculas
    planetas[-4:] = [planeta.upper() for planeta in planetas[-4:]]

    # Verificar si "SATURNO" pertenece a la lista
    saturno_pertenece = "SATURNO" in planetas

    # Verificar si "plutón" pertenece a la lista
    pluton_pertenece = "plutón" in planetas

    # Mostrar la lista original, la sublista y las variables booleanas
    print("Lista original:", planetas)
    print("Sublista de planetas rocosos:", planetas_rocosos)
    print("¿SATURNO pertenece a la lista?:", saturno_pertenece)
    print("¿plutón pertenece a la lista?:", pluton_pertenece)

if __name__ == "__main__":
    main()