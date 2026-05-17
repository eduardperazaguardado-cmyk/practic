nombre_completo = input("Ingresa tu nombre y apellido: ")

lista_nombres = nombre_completo.split()

lista_invertida = lista_nombres[::-1]

for palabra in lista_invertida:

    for letra in palabra:
        print(letra, end=".")

    print()
