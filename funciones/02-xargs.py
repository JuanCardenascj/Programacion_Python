'''Xargs'''

#Define la funcion
def suma(*numeros): #Parametro en plural - * se trata de algo iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
    
suma(2, 5)
suma(3,6,7)