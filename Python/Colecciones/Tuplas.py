'''
Tuplas : Son listas inmutables, no pueden ser modiicadas
'''

#Ejemplo - Solo le agregan unos unicos valores, para siempre

tupla = (4,"hola",6.78,[1,2,3],5) #Se pueden agregar multiples valores

print(4 in tupla) #Todo tipo de busqueda esta permitido

#Transformar o convertir tuplas en listas o listas en tuplas

tupla2 = (3,4,"soo",5,6)
lista = list(tupla) #Metodo para ser convertida en lista

print(lista)

lista2 = (3,4,"soo",5,6)
tupla3 = tuple3(lista) #Metodo para ser convertida en una tupla

print(lista)