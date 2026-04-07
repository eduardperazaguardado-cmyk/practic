texto = input("Ingrese un texto: ")
opcion = int(input("Elija una opción (1: mayúscula, 2: minúscula, 3: capitalizar): "))


def texto_transformado(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida. Por favor, elija 1, 2 o 3."


print(texto_transformado(texto, opcion))
