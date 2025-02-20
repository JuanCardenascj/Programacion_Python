'''Alcance'''

#Variable Global - No utilizar variables globales
saludo = "Hola Global" #Dicen que es una mala practica 

#Primero se define la variable y luego se llama
def saludar():
    saludo = "Hola people"
    print(saludo)
    
#Primero se define la variable y luego se llama    
def saludaPeople():
    saludo = "Hola Jovenes"
    print(saludo)
    
#Primero se define la variable y luego se llama    
def saluda(): #Pesima practica de variable
    global saludo #No usar variables globales
    saludo = "Hola generaciones"
    print(saludo)
        
print(saludo)        
saludar()
print(saludo)
