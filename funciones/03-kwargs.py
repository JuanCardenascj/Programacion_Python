'''Kwargs'''

#Esto es un diccionario
def get_product(**datos): #Def - definir una funcion
    print(datos["id"], datos["name"]) #Datos a imprimir con iteracion
    
get_product(id="id", name="iphone", desc="Esto es un iphone")
