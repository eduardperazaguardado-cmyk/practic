texto = input("Ingrese un texto: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))


def validar_opcion(texto, numero):

    if numero not in [1, 2, 3]:

        print("opcion invalida")


validar_opcion(texto, numero)
