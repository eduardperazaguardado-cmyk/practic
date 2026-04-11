# Cadena original
texto = "  el nido matinal  "

# Quitar espacios y poner mayúscula en cada palabra
texto_limpio = texto.strip()
texto_separado = texto_limpio.title()

print(texto_separado)

# Centrar en 30 caracteres con guiones "-"
resultado = texto_separado.center(30, "-")

print(resultado)
