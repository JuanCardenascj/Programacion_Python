'''
Determina si un año es bisiesto 
Regla de negocio
     -divisible por 4
     -no divisible por 100
     -divisible por 400
'''
#Ejercicio resuelto - solucion
anio = 2024

if (anio % 4 == 0 and anio % 100 != 0) or \
    (anio % 400 == 0):
    print('Es un año bisiesto')
else:
    print('No es bisiesto')