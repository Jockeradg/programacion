class Hipoteca:
    """
    Clase que representa una hipoteca.
    Atributos:
        __porcentaje_tipo_interes_anual (float): Porcentaje del tipo de interés anual.
        __capital (float): Capital de la hipoteca.
        __numero_mensualidades (int): Número de mensualidades.
        __entidad_bancaria (str): Nombre de la entidad bancaria.
    """

    def __init__(self, porcentaje_tipo_interes_anual: float, capital: float, 
                 numero_mensualidades: int, entidad_bancaria: str):
        """
        Genera un objeto con información necesaria para calcular una hipoteca.
        Args:
            porcentaje_tipo_interes_anual (float): Porcentaje del tipo de interés anual.
            capital (float): Capital de la hipoteca.
            numero_mensualidades (int): Número de mensualidades.
            entidad_bancaria (str): Nombre de la entidad bancaria.
        """
        self.__tipo_interes_anual = porcentaje_tipo_interes_anual / 100
        self.__capital = capital
        self.__numero_mensualidades = numero_mensualidades
        self.__entidad_bancaria = entidad_bancaria

    def calcular_pago_mensual(self)->float:
        """
        Calcula el pago mensual de la hipoteca.

        Returns:
            (float): Devuelve el pago mensual de la hipoteca.
        """
        tipo_interes_mensual = self.__tipo_interes_anual / 12
        return self.__capital * tipo_interes_mensual / (1 - (1 + tipo_interes_mensual) ** -self.__numero_mensualidades)
   
def main():
    # Crear un objeto de la clase Hipoteca usando valores literales para los parámetros
    hipoteca_1 = Hipoteca(200000, 0.05, 30, "BBVA")

    # Crear un segundo objeto de la misma clase pero usando valores leídos del teclado
    capital = float(input("Ingrese el monto de la hipoteca: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual: "))
    plazo = int(input("Ingrese el plazo en años: "))
    banco = input("Ingrese el nombre del banco: ")
    hipoteca_2 = Hipoteca(tasa_interes, capital, plazo,banco)

    # Mostrar en pantalla el pago mensual a realizar con ambos objetos
    pago_mensual1 = hipoteca_1.calcular_pago_mensual()
    pago_mensual2 = hipoteca_2.calcular_pago_mensual()
    print("El pago mensual para la hipoteca 1 es:", pago_mensual1," euros")
    print("El pago mensual para la hipoteca 2 es:", pago_mensual2," euros")


if __name__ == "__main__":
    main()