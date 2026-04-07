texto = input("Ingrese un texto: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))


def transformar_Y_Contar(texto, numero):
    if numero not in [1, 2, 3]:
        return "opcion invalida"
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()

    cantidad_caracteres = len(resultado)
    return cantidad_caracteres


print(transformar_Y_Contar(texto, numero))
