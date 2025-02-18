'''
Operadores Lógicos:

   Permiten construir expresiones lógicas, se obtiene como resultado booleanos:
   
   1. And(Conjunción) and
   2. Or(Disyunción) or
   3. Negación not
   
   Operador AND: (Es una multiplicacion Lógica)
   Para que sea verdadero debe ser verdadero True and True = True
   Si varia verdadero and falso o falso and falso o falso and verdaero SIEMPRE SERA FALSE
   
   Operador OR: (Es una Suma Lógica)
   Para que sea verdadero debe tener al menos un True en la comparacion 
   Ejemplo: True or True = true
            True or False = true
            False or True = true
   Para que sea falso o false debe ser que ambas sean falsas al comparar
   Ejemplo: False or Flase = false
   
   Operador NEGACION: (Not)
   Para que sea false, se debe negar un True para que sea falso
   Para que sea verdaero, se debe negar un False para que sea verdadero
   
   Prioridad de los operdaores Lógicos
     1.NOT
     2.AND
     3.OR
     
     Prioridad de los Operadores en General
     1. ()
     2. **
     3. *, /, mod, not
     4. +, -, and
     5. >, <,  ==, >=, <=, !=, or
'''

#Operador Lógicos 
    
    #Ejemplo a resolver
a = 10 #a = 10 #a es mayor a b (a > b) es False
b = 12 #b = 12 #a es menor a c (a < b) es True
c = 13 #c = 13 #a es igualdad a c (a == c) es False
d = 10 #d = 10 #a es mayor o igual a b ( a >= b)  es False

#Colocamos la variable resultado y:
resultado = ((a > b) or ( a < c)) and ((a == c) or (a >= b))  #Entonces Verificamos
            #FALSE       #TRUE         #FALSE       #FALSE
                   #TRUE                      #FALSE
                                 #FALSE
print(resultado)

 #Otros Ejemplos.
 
   #Operador Lógico AND
e = 10 #e es igual a 10 
f = 14 #f es igual a 14
g = 20 #g es igual a 20

#Para que sea verdadero en AND ambas declaraciones deben ser Verdaderas
resultado = ((e < f) and (f < g)) #Entonces verificamos segun el Operador
             #True        #True
                    #True    
#Para que sea falso en AND una declaracion deben ser Verdadera y la otra Falsa
resultado = ((e > f) and (f < g)) #Entonces verificamos segun el Operador
             #False        #True
                    #False  

print(resultado)

#Operador Lógico OR
e = 10 #e es igual a 10 
f = 14 #f es igual a 14
g = 20 #g es igual a 20

#Para que sea verdadero en OR una declaraciones debe ser Verdadera y la otra falsa
resultado = ((e > f) or (f < g)) #Entonces verificamos segun el Operador
             #False        #True
                    #True    
#Para que sea falso en AND una declaracion deben ser Falsa y la otra Falsa
resultado = ((e > f) and (f < g)) #Entonces verificamos segun el Operador
             #False        #False
                    #False  

print(resultado)

#Operador Lógico NOT
e = 10 #e es igual a 10 
f = 14 #f es igual a 14
g = 20 #g es igual a 20

#Para que sea verdadero en OR una declaraciones debe ser Verdadera y la otra falsa
resultado = not((e > f) or (f < g)) #Entonces verificamos segun el Operador
             #False        #True
                    #True    
#Para que sea falso en AND una declaracion deben ser Falsa y la otra Falsa
resultado = ((e > f) and (f < g)) #Entonces verificamos segun el Operador
             #False        #False
                    #False  

print(resultado)
