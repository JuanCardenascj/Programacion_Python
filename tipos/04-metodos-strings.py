'''
Metodos String
'''

#Ejemplo

animal = "Chanchito feliz"

#upper es el metodo - lo convierte en mayusculas
print(animal.upper()) 

#Lower es el metodo - lo convierte en minusculas
print(animal.lower()) 

#Capitalize - Convierte el primer caracter en mayuscula
print(animal.capitalize())

#Title es el metodo - toma la primera letra de cada palabra y las convierte en mayuscula 
print(animal.title())

 #Strip  es el meotod - remueve los espacios entre izquierda y derecha 
print(animal.strip())

#Find es el metodo - sirve para buscar una letras o letras que nosotros le indiquemos
print(animal.find("Ch"))

#Replace es el metodo- para reemplazar caracteres que se le indican
print(animal.replace("ch", "jh"))

# "" in animal - Busca el valor indicado y te devuelve un boolean
print("ch" in animal)

# "" not in animal - Busca el valor indicado y lo niega para devolver un booleano
print("ch" not in animal)
 
#Encadenamos los metodos
print(animal.capitalize().capitalize())
