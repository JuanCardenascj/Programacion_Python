'''
Conjuntos: Grupos de elementos desordenados (No pueden existir duplicados)
'''

#Ejemplo - Dnetro de los conjuntos no puede existir otra coleccion

conjunto = set() #Con set ya le dice a python que es un conjunto

conjunto = {1,2,3,"Hola",4,5.54} #Esto seria un diccionario

conjunto.add(5) #Agrega valores
conjunto.add("Adios") #Agrega valores
conjunto.add('a') #Agrega valores
conjunto.discard("Hola") #Para eliminar valores
conjunto.clear() #Para vaciar el conjunto


print(conjunto)

#Otro Ejemplo de Conjuntos - Los valores son unitarios

a = {1,2,3}
b = {3,4,5}

print(a == b) #Evalua la igualdad y es falso

c = a | b #Define | union de conjuntos

print(c) 

d = a & b #Es la interseccion de los conjuntos

print(d)

e = a - b #Diferencia de conjuntos

print(e)

f = a ^ b #Diferencia Simetrica

print(f)