'''
Ejercicio 3:

   Hacer un programa que pida un carácter e indique si es un vocal o no.
   
'''

#Solucion - Operadores Relacionales, Operadores logicos

letra = input("Digite un caracter: ").lower #Para transformar a minuscula

#Condicionales
if letra == 'a' or letra == 'b' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es una vocal")
else:
    print("No es una vocal")