class Hipoteca:
    def __init__(self, capital, interes_anual, numero_mensualidades):
        self.capital = capital
        self.interes_anual = interes_anual
        self.numero_mensualidades = numero_mensualidades

    def calcular_pago_mensual(self):
        interes_mensual = self.interes_anual / 12
        pago_mensual = (self.capital * interes_mensual) / (1 - (1 + interes_mensual) ** -self.numero_mensualidades)
        return pago_mensual

# Example usage
hipoteca = Hipoteca(100000, 0.05, 12)
pago_mensual = hipoteca.calcular_pago_mensual()
print(f"El pago mensual de la hipoteca es: {pago_mensual} euros")