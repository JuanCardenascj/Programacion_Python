'''Depuracion'''

def largo(texto): #Calcula la longitud o la cantidad de caracteres del texto
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado 
    
print("Chanchito") #CLIC PUNTO ROJO - RED POINT
l = largo("Hola gente")
print(l)