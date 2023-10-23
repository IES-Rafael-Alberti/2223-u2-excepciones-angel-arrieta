def cuentaAtras(inicio: int) -> str:
    resultado = ""
    for n in range(inicio, -1, -1):
        resultado += f"{n}, "
    return resultado[:-2]


if __name__ == "__main__":
    inicioValido = False
    while not inicioValido:
        try:
            # Entrada
            primer_numero = input("¿Desde que número comenzamos la cuenta atras?\t")
            primero_util = int(primer_numero)
            if primero_util < 1:
                raise ValueError
            inicioValido = True
        except ValueError:
            print("Introduzca un inicio de cuenta lógico")
    # Proceso
    cuenta_regresiva = cuentaAtras(primero_util)
    # Salida
    print(cuenta_regresiva)
