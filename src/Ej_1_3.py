def unaVida(edad: int):
    resultado = ""
    for anos in range(edad):
        resultado += f"{anos + 1}\n"
    return resultado[:-1]


if __name__ == "__main__":
    try:
        # Entrada
        edad_actual = int(input("Introduzca su edad\t"))
        # Proceso
        recorrido_vida = unaVida(edad_actual)
        # Salida
        print(recorrido_vida)
    except ValueError:
        print("Por favor, introduzca un número")
