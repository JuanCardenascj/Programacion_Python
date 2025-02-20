#Ejemplo

mascotas = [
    "pelusa", 
    "pulga", 
    "felipe", 
    "jhorman"
]

#Agregar nuevo valor INSERT
mascotas.insert(1, "Yilbert")
mascotas.append("Alexander")#Comodar al final de la lista


mascotas.remove("Alexander")#Eliminar elemento pero elimina el primero en la lista
mascotas.pop(1)#Elimina un elmento en particular
del mascotas[0]#Elimia el primer elemento de la lista
mascotas.clear()#Eliminar la lista completa
print(mascotas)