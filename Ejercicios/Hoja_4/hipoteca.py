class Hipoteca:
    def __init__(self, porcentaje_tipo_interes_anual: float, capital: float, numero_mensualidades: int, entidad_bancaria: str):
        """
        Constructor de la clase Hipoteca.
        Args:
            porcentaje_tipo_interes_anual (float): Porcentaje del tipo de interés anual.
            capital (float): Capital de la hipoteca.
            numero_mensualidades (int): Número de mensualidades.
            entidad_bancaria (str): Nombre de la entidad bancaria.
        """
        self.tipo_interes_anual = porcentaje_tipo_interes_anual / 100
        self.capital = capital
        self.numero_mensualidades = numero_mensualidades
        self.entidad_bancaria = entidad_bancaria