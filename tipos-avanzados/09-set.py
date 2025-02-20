'''Es una coleccion de datos que no se puede repetir y esta ordenada
     
     Operadores de los SETS!
     | -> Union
     & -> Interseccion
     - -> Diferencia
     ^ -> Diferencia Simetrica
      

'''

#Ejemplo

primer = {1,1,2,2,3,4}
primer.add(5)#Agregar un elemento
primer.remove(1)#Remueve el elemento
print(primer)


segundo = {3,4,5}
segundo = set(segundo)
print(segundo) #Un set en base a una lista
