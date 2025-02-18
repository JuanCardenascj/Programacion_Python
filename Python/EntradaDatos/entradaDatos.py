'''
Entrada de datos desde la consola
'''
#ENTRADA DE DATOS - EJEMPLOS

'''Datos de tipo Cadena'''
#Se crea la variable donde almancena el valor
nombre = input("Digite su nombre: ") #Pide y guarda los datos ingresados por el usuario
apellido = input("Digite su apellido: ") #Pide y guarda los datos ingresados por el usuario
grado = input("Digite su grado escolas: ") #Pide y guarda los datos ingresados por el usuario

print(f"Hola {nombre} {apellido} {grado}") #Imprime Hola, y le pide digitar su nombre y apellido

'''Datos de tipo Numeros'''
#Se crea la vairbale donde almacena el numero
numero = int(input("Digite un numero: ")) #Pide y guarda los datos ingresados por el usuario
numero2 = float(input("Digite un numero real: ")) #Pide y guarda los datos ingresados por el usuario

print(f"Los numeros ingresados son: {numero} y {numero2}")