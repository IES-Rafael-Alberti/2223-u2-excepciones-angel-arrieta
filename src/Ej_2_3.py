def example(ejemplo):
    ejemplo = None
    return ejemplo


if __name__ == "__main__":
    try:
        # Entrada
        entrada = str(input(">\t"))
    except ValueError:
        print("")
    # Proceso
    procesado = example(entrada)
    # Salida
    print(procesado)
