Algoritmo Numero_Mayor_O_Menor
	definir PrimerValor, SegundoValor Como Entero
	escribir "ingrese un numero"
	leer PrimerValor
	escribir "ingrese otro numero"
	leer SegundoValor
	
	si PrimerValor > SegundoValor entonces 
		escribir " Primer valor es mayor "
	SiNo
		si SegundoValor > PrimerValor Entonces
			escribir " Segundo valor es mayor"
		FinSi
		
		si PrimerValor = SegundoValor Entonces
			escribir "son iguales"
		FinSi
	FinSi
	
FinAlgoritmo