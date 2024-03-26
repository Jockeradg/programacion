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