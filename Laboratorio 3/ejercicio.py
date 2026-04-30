menu = True
while menu:
    print("BIBLIOTECA")
    print("1. Procesar libros Prestados")
    print("2. Salir")

    accion = input("Accion a realizar: ")

    match accion:
        case "1":
            libros = int(input("Cuantos libros va a registrar? "))
            for i in range(libros):
                prestamo = input(f"¿El libro {i + 1} es para prestamo? (si/no): ")
                if prestamo == "si":
                    print("REgistrado como prestado")
                if prestamo == "no":
                    print("Consultar en sala")
                else:
                    print("Opcion no valida, intente de nuevo")

        case "2":
            menu = False
            print("Saliendo de la biblioteca")
        case _:
            print("Opcion no valida, intente de nuevo")
