'''
Invertir una cadena 

         Metodo utilizado para invertir la cadena es
         [::1] Es una técnica conocida como slicing (corte o rebanado)
         
         Cuando usamos el formato de slicing inicio:fin:paso, estamos tomando un "trozo" de la cadena. Pero en este caso, no estamos especificando el inicio ni el fin, solo el paso, que es -1. Aquí es lo que significa:

Inicio y fin vacíos: No se ha indicado ni el inicio ni el fin, lo que significa que se tomará toda la cadena, desde el primer al último carácter.
Paso -1: El paso -1 indica que queremos recorrer la cadena de atrás hacia adelante, es decir, invertirla.
      
'''
#Ejercicio resuelto - solucion
cadena = 'cadena Texto'
invertir = cadena[::-1] #-1 Indica que queremos recorrer la cadenade atras hacia adelante

print("La cadena invertida es: ", invertir)

#Ejercicio resuelto - solucion
cadena2 = 'Caden Textoo'
invertir2 = cadena2[::-1] #[INICIO:FIN:PASO]

print("La cadena invertida es: ", invertir2)

#Ejercicio resuelto - solucion
Cadena3 = 'Ejemplo char para cadenas'
invertir3 = Cadena3[::-1]

print("La cadena invertida es: ", invertir3)

#Ejercicio resuelto - solucion
cadena4 = 'Ejemplo cadena para cadenas 123'
invertir4 = cadena4[::-1]

print("La cadena invertida es: ", invertir4)

#Ejercicio resuelto - solucion
cadena5 = 'Example for to you'
invertir5 = cadena5[::-1]

print("La cadena invertida es: ", invertir5)