class ParteTrabajo:
    """ 
        Contiene los datos de un parte de trabajo de un trabajador

        Attributes:
            __horas: las horas trabajadas
            __trabajador: el nombre del trabajador
            __dia: el día de la semana (“lunes”, “martes”, “miércoles”, ...)
    """

    def __init__(self, horas: int, trabajador: str, dia: str):
        """ 
        Crea un parte dadas las horas trabajadas, el nombre del
        trabajador y el día de la semana
        
        Args:
                 horas: las horas trabajadas
                 trabajador: el nombre del trabajador
                 dia: el día de la semana (“lunes”, “martes”, “miércoles”, ...)
        """
        self.__horas: int = horas
        self.__trabajador: str = trabajador
        self.__dia: str = dia.lower()  # Guardamos el día en minúsculas

    def get_horas(self) -> int:
        """ 
        Retorna las horas trabajadas en un día
        """
        return self.__horas

    def get_dia_semana(self) -> str:
        """ 
        Retorna el día de la semana del parte "lunes, "martes, …
        """
        return self.__dia

    def get_trabajador(self) -> str:
        """ 
        Retorna el nombre del trabajador
        """
        return self.__trabajador

def calcular_total_horas(partes_trabajo: list) -> int:
        """
        Calcula el número total de horas trabajadas en todos los partes de trabajo de la lista.

        Args:
            partes_trabajo: una lista de objetos de la clase ParteTrabajo

        Returns:
            El número total de horas trabajadas en todos los partes de trabajo de la lista.
        """
        total_horas = 0
        for parte in partes_trabajo:
            total_horas += parte.get_horas()
        return total_horas

def main():
        """
        Función principal para probar la función calcular_total_horas.
        """
        partes_trabajo = [
            ParteTrabajo(8, "Juan", "lunes"),
            ParteTrabajo(6, "María", "martes"),
            ParteTrabajo(7, "Pedro", "miércoles"),
            ParteTrabajo(5, "Ana", "jueves"),
            ParteTrabajo(9, "Luis", "viernes")
        ]
        total_horas = calcular_total_horas(partes_trabajo)
        print(f"El número total de horas trabajadas es: {total_horas}")

if __name__ == "__main__":
    main()        