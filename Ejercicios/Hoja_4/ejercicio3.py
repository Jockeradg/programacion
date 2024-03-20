class Hipoteca:
    def __init__(self, monto, tasa_interes, plazo):
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo = plazo

    def calcular_pago_mensual(self):
        tasa_mensual = self.tasa_interes / 12
        plazo_meses = self.plazo * 12
        pago_mensual = (self.monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo_meses)
        return pago_mensual


def main():
    # Crear un objeto de la clase Hipoteca usando valores literales para los parámetros
    hipoteca1 = Hipoteca(200000, 0.05, 30)

    # Crear un segundo objeto de la misma clase pero usando valores leídos del teclado
    monto = float(input("Ingrese el monto de la hipoteca: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual: "))
    plazo = int(input("Ingrese el plazo en años: "))
    hipoteca2 = Hipoteca(monto, tasa_interes, plazo)

    # Mostrar en pantalla el pago mensual a realizar con ambos objetos
    pago_mensual1 = hipoteca1.calcular_pago_mensual()
    pago_mensual2 = hipoteca2.calcular_pago_mensual()
    print("El pago mensual para la hipoteca 1 es:", pago_mensual1)
    print("El pago mensual para la hipoteca 2 es:", pago_mensual2)


if __name__ == "__main__":
    main()