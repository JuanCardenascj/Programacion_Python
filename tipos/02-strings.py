'''
         Strings:
'''

#Ejemplo
nombre_curso = "Aprendizaje Python"
descripcion_curso = """Es la forma en la podemos escribir la descripcion del string
si lo deseamos para dar un descripcion acerca del mismo string y se pueda ver o mostrar 
en el momento que se imprima en consola"""

print(len(nombre_curso)) #Cuenta la cantidad de caracteres que existen en el nombre del curso
print(nombre_curso[17]) #Para acceder a la letra que se encuentra en la ubicacion numerica registrada
print(nombre_curso[0:18]) #Define desde donde quiere leer : y donde quiere terminar de leer
print(nombre_curso[0:]) #Cuando solo se le da el primer valor, imprime apartir de ese valor e imprime todo 
print(nombre_curso[:18]) #Cuando solo se le pasa el segun valor, imprime el ultimo valor hasta el primero
print(nombre_curso[:]) #Genera una copia del string o el nombre del curso