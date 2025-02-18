'''
Ejercicio 3:
     
     ((3+5x8)<3 and ((-6x4 / 3) + 2 <2)) or (a>b)
     
'''
#Solucion

a = float(input("a -> ")) #Solicita los valores la usuario 
b = float(input("b -> ")) #Solicita los valores la usuario

resultado = ((3 + 5 * 8) <3 and ((-6 / 3 *4) + 2 <2)) or (a > b)

print(f"El resultado es: {resultado}")

