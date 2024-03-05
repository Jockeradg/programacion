def temperatura_solido(temp_inicial: float, tiempo: float, k: float) -> float:
    Ta = temp_ambiente()
    T = Ta + (temp_inicial - Ta) * exp(-k * tiempo)
    return T