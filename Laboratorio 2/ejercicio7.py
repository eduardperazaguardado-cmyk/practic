texto = input("Ingrese un texto: ")
lista_numeros = input("Ingrese una lista de numeros entre 1 y 3 separados por coma: ")


def transformar_en_cadena(texto_original, entrada_numeros):
    numeros = entrada_numeros.split(",")
    resultado = texto_original
    for n in numeros:
        n = n.strip()
        if n == "1":
            resultado = resultado.upper()
        elif n == "2":
            resultado = resultado.lower()
        elif n == "3":
            resultado = resultado.capitalize()
        else:
            return "Número no valido"
    return resultado


print(transformar_en_cadena(texto, lista_numeros))
