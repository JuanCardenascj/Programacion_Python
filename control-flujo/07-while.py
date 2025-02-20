'''
WHILE - MIENTRAS
'''
#Ejemplo - While
numero = 1 #Numero vale 1
while numero < 100: # Mientras que numero que es igual a 1, sea menor a 100
    print(numero) #Imprima la variable numero
    numero *= 2 # A la variable numero multipliquele por 2 hasta que sea menor que 100 - osea un numero antes del 100
    
'''
LOOPS INFINITOS : Es cuando no tenemos una condicion de salida
'''

#Ejemplo - LOOPS
comando = ""

while True:
    comando = input ("$")
    print(comando)
    if comando.lower() == "salir":
        break
    