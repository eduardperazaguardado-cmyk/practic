Serie = "Fullmetal alchemits"
### Cada variable tiene un espacio de memoria asignado

## cuando una variable cambia => se pierde la inmutabilidad

## es un arreglo, es una variable que tiene adentro otra variable
## Listas<>
## Arrays<>  -> se iniicia a contar desde el 0
## tuplas<>
## indices
# ----------------------------------------

# POO
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo
## abstracciones ->
#     Tasa de cafe
#      Cafe coscafe
#     azucar
## un objeto es el que toma un modelo y este
##  modelo le da funciones y utilizaa sus propiedades
# ------------------------------------------
## Uso de polimorfismo : maneja = Clases y Estructura de datos
# -------------------------------------------


def saludo(nombres):
    print(nombres)


# saludo(Serie) las funciones siempre van a tener ()
# -------------------------------

saludo(Serie)
## las funciones tienen un espacio
## a lo que se llama "Scope"
##Scope es donde reciden las variables

# Colocar el nombre de la serie como titulo
fmaTemu = Serie.title()
saludo(Serie)
# saludo(fmaTemu)
fnaMayusculas = Serie.upper()
saludo(fnaMayusculas)
##programción lineal (Ejemplo)

FullmetalCapitalizer = fnaMayusculas.swapcase().title()
## cuando encadenamos funciones que se indica que la
##  salida de la funcion actual es la entrada de la
##   siguiente funcion

saludo(FullmetalCapitalizer)

##comparar cadenas de texto
comparar1 = "eduard"
comparar2 = "eduard"

varaiabletemporal1 = comparar2.casefold()
comparar = comparar1.casefold() == comparar2.casefold()


clasicas2005 = "Gasolina 2025 "
comprarisAlpha = clasicas2005.isalpha()
print(comprarisAlpha, 2005)

# Isalpha nos va a dar true si el string que se le esta dando es unicamente letras


## si solo quiero numero  isalnum

letraCancion = " Lo que paso, paso, entre tu y yo"  # 3 no tengo numero
decada = "10"

ejemplo = letraCancion.isalnum()
# print(ejemplo)
ejemplo = decada.isalnum()
# print(ejemplo)


comprobarDecadas = decada.isdigit()
print(comprobarDecadas)
