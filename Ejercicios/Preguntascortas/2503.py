def calcula_pago(precio, unidades):
    descuento = 0.0
    if unidades > 20:
        descuento = 0.10
    elif unidades > 10:
        descuento = 0.05
    return precio * unidades * (1 - descuento)