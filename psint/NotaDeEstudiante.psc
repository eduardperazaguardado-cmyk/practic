Algoritmo NotaDeEstudiante
	definir calificacion como Entero
	
	escribir " Ingrese su calificacion  "
	Leer calificacion
	
	si calificacion > 10 Entonces
		Escribir "Nota invalida"
		si calificacion < 0 Entonces
			Escribir "Nota invalida"
		Sino si calificacion >= 6 Entonces
			escribir "Aprobado"
		Sino si calificacion <= 4 Entonces
			Escribir "reprobado"
		Sino si calificacion = 5 Entonces
			Escribir "recuperacion"
		FinSi
	FinSi
FinSi
FinSi
FinSi

FinAlgoritmo