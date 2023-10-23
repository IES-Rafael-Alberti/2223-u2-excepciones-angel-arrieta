def unaVida(edad: int):
    resultado = ""
    for anos in range(edad):
        resultado += f"{anos + 1}\n"
    return resultado[:-1]


if __name__ == "__main__":
    # Entrada
    edad_actual = int(input("Introduzca su edad\t"))
    try:
        # Proceso
        recorrido_vida = unaVida(edad_actual)
        # Salida
        print(recorrido_vida)
    except ValueError:
        print("Por favor, introduzca un número")
