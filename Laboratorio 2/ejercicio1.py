texto = input("Ingrese un texto: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))


def funcion(texto, numero):

    if numero == 1:
        return texto.upper()

    if numero == 2:
        return texto.lower()

    if numero == 3:
        return texto.capitalize()


print(funcion(texto, numero))
