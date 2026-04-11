# Nombre de archivo
archivo = "Eduard.txt"

# Quitar el sufijo ".txt"
limpio = archivo.replace(".txt", "")

# Quitar el prefijo "ING. "
limpio = limpio.replace("ING. ", "")

# Convertir a minúsculas
resultado = limpio.lower()

print(resultado)
