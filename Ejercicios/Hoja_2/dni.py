def validar_dni(dni)->bool:
    # Comprobar si el DNI comienza por una cifra numérica
    comienza_con_cifra = dni[0].isdigit()

    # Comprobar si el DNI acaba en una letra mayúscula
    acaba_con_mayuscula = dni[-1].isupper()

    # Comprobar si el DNI tiene 9 caracteres
    tiene_9_caracteres = len(dni) == 9

    # Realizar operaciones lógicas con los tres booleanos obtenidos
    resultado = comienza_con_cifra and acaba_con_mayuscula and tiene_9_caracteres

    return resultado

#Solución
def comprobar_dni(dni:str)->bool:
    comienzo:bool = '0' <= dni[0] <= '9'
    final:bool = 'A' <= dni[-1] <= 'Z'
    largo:bool = len(dni) == 9
    return comienzo and final and largo