
Algoritmo bucle
	// bucle es algo que se repite hasta que
	// una condicion logica la rompe 
	Escribir  "password "
	leer pass
	Mientras pass <> "nombre de ella + fecha especial"   // ! = <> < >
		Escribir  "romper bucle infinito 1 si 2 no "
		leer respuesta
		si respuesta == "si"
			pass = "nombre de ella + fecha especial"
		FinSi
	FinMientras
	
	Escribir  "final"
FinAlgoritmo
