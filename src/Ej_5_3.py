def contrasena(usuario: str) -> bool:
    if usuario == "contrasena":
        respuesta = True
    else:
        respuesta = False
    return respuesta


if __name__ == "__main__":
    contrasenaValida = False
    while not contrasenaValida:
        try:
            # Entrada
            usuario_introduce = input("Introduce la contraseña\n")
            entrada_util = str(usuario_introduce)
            # Proceso
            contrasenaValida = contrasena(entrada_util)
            if contrasenaValida == False:
                raise NameError
            else:
                continue
        # Salida
        except NameError:
            print("Incorrect Password!!")
