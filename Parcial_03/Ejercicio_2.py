from decimal import Decimal

total = Decimal("0")

while True:
    try:

        entrada = input("Ingrese el precio del producto (0 para salir): ")
        precio = Decimal(entrada)

        if precio == 0:
            break

        total += precio

    except ValueError:
        print("Error: debe ingresar un número válido.")

    except:
        print("Error: entrada inválida.")


print(f"El total acumulado es: ${total}")
