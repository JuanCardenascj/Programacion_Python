'''
Ejercicio 5: 
     
     Hacer un programa que simule un cajero automatico con un saldo
     inicial de $1000 y tendrá el siguiente menú de opciones:
     
     1. Ingresar dinro en la cuenta
     2. Retirar dinero de la cuenta
     3. Mostrar dinero disponible
     4. Salir
     
'''

#Solucion

print("Bienvenidos a su cajero aumatico Banco Cardenas")
saldo = 1000

print("       :.MENU:. ")
print(" 1. Ingresar dinero en la cuenta")
print(" 2. Retirar dinero de la cuenta")
print(" 3. Mostrar dinero disponible en la cuenta")
print(" 4. Si usted desea salir")
opcion = int(input("Digite la operacion que usted desea realizar del menú: "))

print()

#Codicionales
if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar ->"))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 2:
    retirar = float(input("Cuanto dinero desea retirar de la cuenta ->"))
    if retirar > saldo:
        print("No tienes los fondos disponibles")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Dinero en la centa: {saldo}")
elif opcion == 4:
    print("Gracias por utilizar su cajero aumatico Banco Cardenas")
else:
    print("Error se equivoco de opcion de menú")
    
        