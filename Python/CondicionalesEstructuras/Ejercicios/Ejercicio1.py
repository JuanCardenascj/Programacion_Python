'''
Ejercicio 1:
 
  Hacer un programa que pida dos numeros y se de cuenta cual de ellos es par o si 
  ambos lo son.
  
'''
#Solucion - Utilizamos operadores aritmeticos, logicos y relacionales

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

#Condicional
if num1 % 2 == 0 and num2 % 2 == 0: #Si numero 1 es divisible entre 2 y es igual a 0 = es par
    print("Ambos son pares")
elif num1 % 2 == 0 and num2 % 2 != 0: #Pero si numero 1 es divisible entre 2 y es igual a 0 and(y) numero 2 es divisible entre 2 pero es diferente de 0  es impar
    print(f"{num1} es par")
elif num1 % 2 != 0 and num2 % 2  == 0: #Pero si numero 1 es divisible entre 2 pero es diferente de 0 es impar and si numero 2 es divisible entre 2 y es igual a 0 es par
    print(f"{num2} es par")
else: #Si ningun cumple la condicon ambos son impares
    print("Ambos numeros son impares")