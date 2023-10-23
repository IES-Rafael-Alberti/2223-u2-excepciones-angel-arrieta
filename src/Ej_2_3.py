def impares(ultimo: int) -> str:
    resultado = ""
    for n in range(0, ultimo, 2):
        resultado += f"{n+1}, "
    return resultado[:-2]


if __name__ == "__main__":
    numeroValido = False
    while not numeroValido:
        try:
            # Entrada
            ultimo_numero = input("Lista de números impares. Dime hasta que número llego\t")
            numero_util = int(ultimo_numero)
            if numero_util <= 0:
                raise ValueError
            numeroValido = True
        except ValueError:
            print("Por favor, introduzca un rango valido")
    # Proceso
    lista_impares = impares(numero_util)
    # Salida
    print(lista_impares)
