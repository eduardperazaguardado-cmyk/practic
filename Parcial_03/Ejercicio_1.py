etiqueta = input("Ingrese la etiqueta de rastreo. Ejemplo:2025-Deportes-SV: ")


if etiqueta == "" or etiqueta is None:
    print("Error: la etiqueta está vacía.")
else:

    primer_guion = etiqueta.find("-")
    ultimo_guion = etiqueta.rfind("-")

    categoria = etiqueta[primer_guion + 1 : ultimo_guion]

    print("Categoría:", categoria)

    print("Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional")
