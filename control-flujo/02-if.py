'''
Condicional IF - SI
           
           El orden de las expresiones dentro de las condicionales
           se deben pensar y organizar bastante bien para que el codigo
           se ejecute correctamente
'''
#edad base
edad = 68

if edad > 65: #Si la edad del usuario es mayor a 17 años
    print("Puede ver la pelicula con Super descuento") #Entonces = 
elif edad > 54:
    print("Puede ver la pelicula con descuento")
elif edad > 17:
    print("Puede ver la pelicula")
else: #Sino es mayor de edad entonces =
    print("No puede ingreasr a ver la pelicuala")
    
print("Listo")