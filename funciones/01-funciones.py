'''
Funciones: 1. Print imprime
           2.
'''

def hola(nombre, apellido): #Parametro de la funcion nombre
    print("Hola gente")
    print(f"Bienvenido {nombre} {apellido}") #Uso de sus parametros
    
hola("Juan", "Cardenas") #Llama la funcion - argumentos

'''Parametros Opcionales'''
def hola2(nombre, apellido="cardenas"): #Parametro de la funcion nombre
    print("Hola gente")
    print(f"Bienvenido {nombre} {apellido}") #Uso de sus parametros
    
#Cuando no se le define el valor del argumento - entonces se define en el parametro    
hola2("Juan") #Llama la funcion - argumentos

'''Argumentos nombrados'''

def hola3(nombre, apellido): #Parametro de la funcion nombre
    print("Hola gente")
    print(f"Bienvenido {nombre} {apellido}") #Uso de sus parametros
    
#Argumento nombrado   
hola3(apellido="Cardenas",nombre="David") #Argumentos

