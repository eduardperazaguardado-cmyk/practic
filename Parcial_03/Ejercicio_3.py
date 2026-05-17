temperaturas = []
for i in range(5):
    temp = int(input(f"Ingrese la temperatura #{i + 1}: "))
    temperaturas.append(temp)

for temp in temperaturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")

        case 100:
            print("Alerta: Punto de Ebullición")

        case _:
            print("Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico")
