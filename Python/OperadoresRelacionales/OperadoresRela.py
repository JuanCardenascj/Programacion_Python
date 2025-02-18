'''
Se utilizan para establecer una relacion entre 2 valores
Comparan estos valores entre si y esta comparacion produce un 
resultado de certeza o falsedad(verdadero o falso).
Tienen el mismo nivel de prioridad en su evaluacion
Los operadores relacionales tiene menor prioridad que los aritmeticos

Por Ejemplo: 
     Si tenemos una operacion combinada de operadores aritmeticos y relaciones combinados
     Los aritmeticos se ejecutan primero y luego los relaciones
     
     ¿Cuales son esos Operadores Relacionales?
     
     1. > Mayor que
     2. < Menor que 
     3. >= Mayor o igual
     4. <= Menor o igual
     5. != Diferente de
     6. == Igualdad a
'''
#Operadores Relacionales

#Operador Relacional Menor Que
resultado = 10 < 20 #10 es menor a 20

print(resultado) #Imprime resultado

'''
Combinaciones con operadores Aritmeticos
'''

a = 10 # a es igual a 10
b = 20 # b es igual a 20
c = 30 # c es igual a 30

#Recordar los operadores aritmeticos Priority
resultado = a + b < c # la suma de a mas b es menor al valor de c
resultado = a - b < c # la resta de a mas b es menor al valor de c
resultado = a * b < c # la multiplicacion de a mas b es menor al valor de c
resultado = a / b < c # la division de a mas b es menor al valor de c
print(resultado)#Imprime

#Operador Relacional Mayor Que
resultado = 10 > 20 #10 es mayor a 20

print(resultado)

'''
Combinaciones con operadores Aritmeticos
'''

a = 10 # a es igual a 10
b = 20 # b es igual a 20
c = 30 # c es igual a 30

#Recordar los operadores aritmeticos Priority
resultado = a + b > c # la suma de a mas b es mayor al valor de c
resultado = a - b > c # la resta de a mas b es mayor al valor de c
resultado = a * b > c # la multiplicacion de a mas b es mayor al valor de c
resultado = a / b > c # la division de a mas b es mayor al valor de c
print(resultado)#Imprime

#Operador Relacional Menor o Igual Que
resultado = 10 <= 20 #10 es menor o igual a 20

print(resultado)

'''
Combinaciones con operadores Aritmeticos
'''

a = 10 # a es igual a 10
b = 20 # b es igual a 20
c = 30 # c es igual a 30

#Recordar los operadores aritmeticos Priority
resultado = a + b <= c # la suma de a mas b es menor o igual al valor de c
resultado = a - b <= c # la resta de a mas b es menor o igual de c
resultado = a * b <= c # la multiplicacion de a mas b es menor o igual de c
resultado = a / b <= c # la division de a mas b es menor o igual de c
print(resultado)#Imprime

#Operador Relacional Mayor o Igual Que
resultado = 10 >= 20

print(resultado)

'''
Combinaciones con operadores Aritmeticos
'''

a = 10 # a es igual a 10
b = 20 # b es igual a 20
c = 30 # c es igual a 30

#Recordar los operadores aritmeticos Priority
resultado = a + b >= c # la suma de a mas b es mayor o igual al valor de c
resultado = a - b >= c # la resta de a mas b es mayor o igual de c
resultado = a * b >= c # la multiplicacion de a mas b es mayor  o igual de c
resultado = a / b >= c # la division de a mas b es mayor o igual de c
print(resultado)#Imprime

#Operador Relacional Diferente de 
resultado = 10 != 20 # 10 es diferente de 20

print(resultado)

'''
Combinaciones con operadores Aritmeticos
'''

a = 10 # a es igual a 10
b = 20 # b es igual a 20
c = 30 # c es igual a 30

#Recordar los operadores aritmeticos Priority
resultado = a + b < c # la suma de a mas b es diferente al valor de c
resultado = a - b < c # la resta de a mas b es diferente al valor de c
resultado = a * b < c # la multiplicacion de a mas b es diferente al valor de c
resultado = a / b < c # la division de a mas b es diferente al valor de c
print(resultado)#Imprime

#Operador Relacional Igualdad A
resultado = 10 == 20 #10 es de igualdad a 20

print(resultado)

'''
Combinaciones con operadores Aritmeticos
'''

a = 10 # a es igual a 10
b = 20 # b es igual a 20
c = 30 # c es igual a 30

#Recordar los operadores aritmeticos Priority
resultado = a + b < c # la suma de a mas b es igualdad al valor de c
resultado = a - b < c # la resta de a mas b es igualdad al valor de c
resultado = a * b < c # la multiplicacion de a mas b es igualdad al valor de c
resultado = a / b < c # la division de a mas b es igualdad al valor de c
print(resultado)#Imprime