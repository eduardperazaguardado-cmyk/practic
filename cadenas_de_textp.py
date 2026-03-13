# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto
cancion = "  "

# textos largos ''' o """
cancion2 = """ Toy mirándote, envolviéndome
Si supieras cómo de mis ojos tú te ves
Lo que quieras, ma, pídelo y ya
Dios para hacerte se tuvo que concentrar, ma
Pa no pensarte a mí me tienen que matar
Como tú no vuelve a nacer otra igual
Y si reencarnamos, te vuelvo a encontrar
Vente, miente
Dime que eres mía solamente
Nuestra conexión es permanente
No quiero a más nadie aunque lo intente
¿Qué se siente
Saber que esto es tuyo solamente?
No puedo sacarte de mi mente
Tú eres mi futuro y mi presente
Baby, tú eres la favorita 'e Dios
Porque te hizo a la perfección
Eso atrás está bien grande como el vagón de una pickup
Me dice pa buscarla y pongo el carro en sport plus
Prendemos pa fumar
Cuando se lo pongo, no lo quiero sacar
Si me vengo, adentro lo vo'a dejar
Ma, tú me tienes que te quiero preñar (uoh-oh)
Hasta en los sueños me sales
He probao a otras, pero como tú no saben
Contigo me dejo ver en público, no importa que nos graben
Tas bien rica, contigo estoy winning
Contigo estoy balling, esa baby es top chef
Vo'a nadar en esa pussy, Michael Phelps
To' los que te hablan mierda de mí es porque como yo quieren ser
Pero ni volviendo a nacer
Baby, desde que te conocí creo en el amor
Aunque a veces me confundes, quiero verte
Así que vente, miente
Dime que eres mía solamente
Nuestra conexión es permanente
No quiero a más nadie aunque lo intente
¿Qué se siente
Saber que esto es tuyo solamente?
No puedo sacarte de mi mente
Tú eres mi futuro y mi presente
Te la echo adentro sin plan B, lo nuestro es love and sex
Si llamas, yo le caigo a donde estés
Toy mal acostumbrao, sin tu presencia ya no sé qué hacer
¿Pa qué engancharme Moissanite? Tú eres mi VVS
No te llegan ni aunque tratan
Piché a toa' estas perras, ma, tú eres mi gata
En la calle es fina, pero en la cama, tremenda sata
Ojalá dure pa siempre nuestra etapa
Tú eres mi reina, siempre te vo'a costear
Hicieron pacto nuestras almas, mami, yo nunca te voy a ghostear
Chíngame como si el mundo va a acabarse
No sabes si mañana va a pasar
Vente, miente
Dime que eres mía solamente
Nuestra conexión es permanente
No quiero más nadie aunque lo intente
¿Qué se siente
Saber que esto es tuyo solamente?
No puedo sacarte de mi mente
Tú eres mi futuro y mi presente"""
print(cancion2)


poema_Mayusculas = cancion2.upper()
print(poema_Mayusculas)

poema_Minusculas = cancion2.lower()
print(poema_Minusculas)

mensaje = "holA Khace prograNDO O Que HaCe"

mensaje_correcto = (
    mensaje.capitalize()
)  # convierte la primera letra en mayuscula y el resto en minuscula
print(mensaje_correcto)

nombre = "messi"
nombre2 = "ronaldo"
comparar = (
    nombre.casefold() == nombre2.casefold()
)  # compara sin importar mayusculas o minusculas
print(comparar)
