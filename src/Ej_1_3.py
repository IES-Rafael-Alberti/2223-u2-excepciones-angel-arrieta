def unaVida(edad: int):
    resultado = ""
    for anos in range(edad):
        resultado += f"{anos + 1}\n"
    return resultado[:-1]


if __name__ == "__main__":
    edadValida = False
    while not edadValida:
        try:
            # Entrada
            edad_actual = input("Introduzca su edad\t")
            edad_util = int(edad_actual)
            edadValida = True
        except ValueError:
            print("Por favor, introduzca una edad valida")

    # Proceso
    recorrido_vida = unaVida(edad_util)
    # Salida
    print(recorrido_vida)
