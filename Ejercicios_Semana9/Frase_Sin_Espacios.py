frase = input("Escribe una frase: ")
frase_sin_espacios = frase.replace(" ", "")
cantidad_caracteres = len(frase_sin_espacios)
print("la frase tiene", cantidad_caracteres, "caracteres sin contar los espacios")
