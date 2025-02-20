'''
Calculadora
'''

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las opciones son suma, resta, multiplicacion, division")

resultado = ""
while True:
    if not resultado: 
        resultado = input("Ingrese números:")
        if resultado.lower == "Salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion")
    if op.lower() == "Salir":
        break
    n2 = input("Ingresa siguiente numero:")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("Operacion no encontrada")
        break
    
    print(f"El resultado es {resultado}")

