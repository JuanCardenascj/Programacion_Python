'''
Pide un numero y verifica si es positivo, negativo o cero
'''

#Ejercicio resuelto - solucion
numero = int(input("Digite un numero"))
if numero == 0:
    print("El numero es 0")
elif numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero no es correcto")
     