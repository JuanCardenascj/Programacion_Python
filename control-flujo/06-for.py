'''
BUCLES : FOR 
       UTILIZADOS PARA ITERAR UNA LISTA DE ELEMENTOS
'''
for numero in range(5): #Range crea una secuencia de numeros 
    print(numero) #Imprime los valores dentro del rango de 0 a 5
    print(numero, numero * 'Hola gente') #Imprime numero 0 a 5 con el string hola gente
    
'''
Bucle: FOR - ELSE
'''

buscar = 3
for numero in range(5): #Para numero en el rango 0 a 4
    print(numero) #Imprima los numros
    #Condicional
    if numero == buscar: #Si numero es igualdad a buscar que seria 3
        print("Encontrado", buscar) # Imprima encontrado y el numero de buscar = 3
        break #Detener la ejecucion del codigo
    else: #Si el numero a buscar = 12 esta fuera del rango entonces
        print("No encontre el número buscado :(") #Imprime.
        
'''
ITERABLES - Range es un iterable
'''

for char in "Ultimate Python":
    print(char) #Imprime cada uno de los caracteres que contiene el String de Python

