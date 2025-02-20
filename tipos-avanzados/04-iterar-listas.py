#Ejemplo Iterar

mascotas = ["pelusa", "pulga", "felipe", "jhorman"]

for mascota in mascotas:
    print(mascota)
    
#Tuplas - accede a los elementos igual que como un listado
for mascota in enumerate(mascotas):
    print(mascota)
    
#Para mostrar la lista iterada con numeros
primero, segundo = [1,2]
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
    