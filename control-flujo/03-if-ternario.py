'''
If - Ternario
'''
#Edad Base
edad = 15

#Condicionales
if edad > 17:
    mensaje = ("Es mayor") #Mensaje permite imprimir el valor del parentesis
else: 
    mensaje = ("Es menor") #Mensaje permite imprimir el valor del parentesis
    
print(mensaje)

#Operador Ternario
mensaje = "Es mayor" if edad > 17 else "es menor"

print(mensaje)