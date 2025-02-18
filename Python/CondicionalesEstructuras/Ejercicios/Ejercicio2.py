'''
Ejercicio 2:

   Hacer un programa que pida 3 numero y determine cual es el mayor
   
'''

#Solucion - Operadores logicos y relacionales

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

#Condicioales
if num1 >= num2 and num1 >= num3: #Si numero1 es mayor o igual a numero dos, y tambien es mayor a numero 3. 
    print(f"El numero mayor es {num1}") #El mayor es numero 1
elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"El numero mayor es {num3}")
    