'''
Condicionales Combinados
'''

#Ejemplo

edad = int(input("Digite su edad: "))

#Condicional
if edad > 0: #Demostrar que si esta vivo, la edad de menos cero es falsa, no existe!
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad") #Condicional anidado, uno dentro de otro
    elif edad < 18:
        print("No es mayor de edad")
        
#Combinamos Condicionales - Operador Logico AND - Ambas condiciones Verdaderas
if edad > 0 and edad < 100: #Demostrar que si esta vivo, la edad de menos cero es falsa, no existe!
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad") #Condicional anidado, uno dentro de otro
    elif edad < 18:
        print("No es mayor de edad")
        
#Combinaciones Condicionales - Operador logico OR - Uno de los dos debe ser Verdadero
if edad > 0 or edad < 100: #Demostrar que si esta vivo, la edad de menos cero es falsa, no existe!
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad") #Condicional anidado, uno dentro de otro
    elif edad < 18:
        print("No es mayor de edad")
        
#Combinaciones Condicionales - Operador logico NOT
if not edad > 0 and edad < 100: #Demostrar que si esta vivo, la edad de menos cero es falsa, no existe!
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad") #Condicional anidado, uno dentro de otro
    elif edad < 18:
        print("No es mayor de edad")