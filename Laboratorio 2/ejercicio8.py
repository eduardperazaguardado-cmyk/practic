def transformar_varias_veces(texto, numeros):
    resultado = texto
    for numero in numeros:
        if numero == "1":
            resultado = resultado.upper()
        elif numero == "2":
            resultado = resultado.lower()
        elif numero == "3":
            resultado = resultado.capitalize()
        else:
            return "Número no válido. Por favor, ingrese 1, 2 o 3."
    return resultado


texto = input("Ingrese un texto: ")
while True:
    print("\n--- Menu de opciones ---")
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Convertir a capitalizado")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "4":
        break
    elif opcion in ["1", "2", "3"]:
        texto = transformar_varias_veces(texto, [opcion])
        print(f"Texto transformado: {texto}")
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
