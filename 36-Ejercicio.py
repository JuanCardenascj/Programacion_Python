'''
Pide un caracter y determina si es una vocal.

         input(): Esta función muestra un mensaje en la pantalla
         y espera que el usuario ingrese algún valor. Lo que el 
         usuario ingresa se almacena como una cadena de texto 
         (un string).
'''

#Ejercicio resuelto - solucion
caracter = input("Ingrese caracter")
vocales = ['a', 'e', 'i', 'o', 'u']

if caracter.lower() in vocales:
    print("Es una vocal")
else:
    print("No es una vocal")
