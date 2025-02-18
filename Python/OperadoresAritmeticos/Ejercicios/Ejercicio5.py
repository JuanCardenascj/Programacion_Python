'''
Ejercicio 5:

     Hacer un programa para ingresar el radio de un circulo
     y se reporte su área y la longitud de la circunferencia.
'''

#Solucion 
import math #Importamos el modulo MATH - aqui esta el valor de pi

radio =  float(input("Digite el radio del circulo: Radio -> ")) #Solicita los valores la usuario
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio


print(f"El área del circulo es: {area:.2f}") #:.2f para indicar que solo quiero ver dos decimales
print(f"La longitud de la circunferencia es: {longitud:.2f}") #:.2f para indicar que solo quiero ver dos decimales
