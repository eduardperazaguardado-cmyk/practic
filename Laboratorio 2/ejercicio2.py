palabra = input("Ingrese una palabra: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))


def transformar(palabra, numero):
    if numero == 1:
        print(palabra.upper())

    elif numero == 2:
        print(palabra.lower())

    elif numero == 3:
        print(palabra.capitalize())

    else:
        print("Número no válido. Por favor, ingrese 1, 2 o 3.")


transformar(palabra, numero)
