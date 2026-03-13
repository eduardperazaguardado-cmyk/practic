Algoritmo Suma_Numeros_Positivos
    Definir numero, suma Como Real
    
    suma <- 0
    
    Repetir
        Escribir "Ingrese un numero (si ingresa un negativo finaliza):"
        Leer numero
        
        Si numero >= 0 Entonces
            suma <- suma + numero
        FinSi
        
    Hasta Que numero < 0
    
    Escribir "La suma de los numeros positivos es: ", suma
    
FinAlgoritmo

