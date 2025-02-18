'''
Listas:
   Podemos almacenar datos numericos, booleanos, etc...
   
   Ejemplo: ["Cadena",Int,float,booleano,[otra lista]]
   
   Es una estrucutura de datos muy flexible
'''
#Ejemplo 
lista = [] #Lista vacia

print(lista)

#Ejemplo - Agregamos valores tipo cadena
lista2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista2)

#Ejemplo 3 - Si queremos mostrar solo un elemento de la lista
lista3 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista2[2]) #Al escribir dicho numero en el indice [1] o [2] o [3]. Ese sera el que mostrara

#Ejemplo 4 - Si queremos mostrar elementos de atras para adelante
lista4 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista4[-1]) #Indica el ultimo elemento que tiene

#Ejemplo 5 - Si queremos que imprima desde el indice 0 al indice 3
lista5 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista5[0:3]) #Imprime los tres primeros elementos

'''
Otros ejemplo de otras cosas que podemos hacer con las listas
'''
#Ejemplo 6 - Funcion len
lista6 = ["Cadena",20,20.5,[1,2,3]] #Es un ejemplo

print(len(lista6)) #Retorna la cantidad de elementos almacenados en la lista

#Ejemplo 7 - Para agregar elementos en la lista
lista7 = [1,2,3,4,5]

lista7.append(6) #Agregar un elemento al final de la lista
lista7.append("Juan David") #Si se quiere agregar otro elemento al final de la lista

print(lista7)

#Agregar otro elemento en una posicion especifica
lista7.insert(2,3) #En la posicion 2 agregas el elemento numero 3

print(lista7)

#Agregar varios elementos al final de la lista - Extend
lista7.extend([6,7,8]) #Extend permite agregar estos tres numeros al final de la lista

print(lista7)

#Queremos sumar dos listas
lista8 = [10,11,12,13]
lista9 = [14,15,16,17]

lista10 = lista8+lista9 #Concatenar las listas

print(lista10)

#Para buscar un elemento dentro de la lista
lista11 = [20,21,22,23,"JuanCJ"]

print(20 in lista11) #El numero 20 se encuentra dentro de la lista 11

#Si quiere saber en que indice se encuentra n valor
lista12 = [2,3,4,5, "JuanDa"]

print(lista12.index(2)) #Imprime el lugar de la lista donde se encuentra
