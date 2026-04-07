lista_de_palabras = input("Escriba una lista de palabras separadas por coma:")
numero = int(input("Ingrese un número (1, 2 o 3): "))


def transformar_lista(entrada, numero):
    if numero not in [1, 2, 3]:
        return "Número no válido. Por favor, ingrese 1, 2 o 3."
    palabras = entrada.split(",")
    resultado = []
    for palabra in palabras:
        p = palabra.strip()  # Eliminar espacios en blanco alrededor de la palabra
        if numero == 1:
            resultado.append(p.upper())
        elif numero == 2:
            resultado.append(p.lower())
        elif numero == 3:
            resultado.append(p.capitalize())
        else:
            return "Número no válido. Por favor, ingrese 1, 2 o 3."
    return ", ".join(resultado)


print(transformar_lista(lista_de_palabras, numero))
