'''
Operadores Logicos: AND OR NOT
                
                and= true true = true / true false = false
                or= true false = true / false false = false
                not= negar el resultado de una operacion
'''

gas = True
encendido = True
edad = 18

#Para el operador logico AND
if gas and encendido:
    print("Puede avanzar")
else: 
    print("No puedes avanzar")

#Para el operador logico OR - FALSE FALSE = FALSE
if gas or encendido:
    print("Puede avanzar")
else: 
    print("No puedes avanzar")

#Para el operador logico NOT 
#EJEMPLO: Si gas: false (NOT LO CAMBIA A TRUE)
#EJEMPLO: Si encendidio: false (NOT LO CAMBIA A TRUE)
if not gas and encendido:
    print("Puede avanzar")
else:                         #Como not cambia los valores a FALSE = False
    print("No puedes avanzar")
    
#EJEMPLO: Si gas: false (NOT LO CAMBIA A TRUE)
#EJEMPLO: Si encendidio: false (NOT LO CAMBIA A TRUE)
if not gas or encendido:
    print("Puede avanzar")
else:                         #Como not cambia los valores a false = false
    print("No puedes avanzar")
    
#OTRO Ejemplo.
if gas and (encendido or edad > 17):
    print("Puedes Avanzar")
else:
    print("No puedes Avanzar")
    
#Otro ejemplo NOT
if not gas and (encendido or edad > 17):
    print("Puedes Avanzar")
