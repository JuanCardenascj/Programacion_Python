'''
Ejercicio 4:

   Construir un programa que simule el funcionamiento de una calculadora que puede realizar
   las cuatro operaciones aritmeticas basicas ( Suma,resta,multipliccion,division). El
   Usuario debe especificar la operacion con el primer caracter del nombre de la operacion.
   
   >. S, s - Suma
   >. R, r - Resta
   >. P, p, M, m - Multiplicacion
   >. D, d - Division
'''

#Solucion - Operadores Aritrmeticos, Operadores Relacionales

print("Bienvenido a tu calculadora por Consola")

num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))

operacion = input("Digite la operacion: ").upper() #Para transforma a mayusculas

#Condicionales
if operacion=='S':
    suma = num1+num2
    print(f" La suma es: {suma}")
elif operacion=='R':
    resta = num1-num2
    print(f" La resta es: {resta}")
elif operacion=='M' or operacion == 'P':
    multiplicacion = num1*num2
    print(f" La multiplicacion es: {multiplicacion}")
elif operacion=='D':
    division = num1/num2
    print(f" La division es: {division:.2f}")
else:
    print("Se equivoco de operacion")