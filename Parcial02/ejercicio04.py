# palabra original
texto = "CANTANDO"

# convertir a minúsculas
texto = texto.lower()

# quitar el sufijo "ando"
texto = texto.replace("ando", "")

# encontrar la posición de la letra "t"
posicion = texto.find("t")

# Mostrar resultados
print(texto)
print(posicion)
