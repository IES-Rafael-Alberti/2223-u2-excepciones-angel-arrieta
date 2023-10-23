def esEntero(numero: int) -> bool:
    if type(numero) == int:
        respuesta = False
    else:
        respuesta = True
    return respuesta


if __name__ == "__main__":
    entradaInvalida = False
    while not entradaInvalida:
        try:
            # Entrada
            entrada = input("Introduce números enteros\t")
            entrada_util = int(entrada)
            # Proceso
            entradaInvalida = esEntero(entrada_util)
        # Salida
        except ValueError:
            print("La entrada no es correcta")
            entradaInvalida = True
