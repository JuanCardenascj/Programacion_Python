'''
Ejercicio5: 
    
    Una tienda ofrece un descuento del 15% sobre el total de la compra
    y un cliente desea saber cuanto debera pagar finalmente por su compra.
    
'''
#Solucion - Compras

valorCompra = float(input("Digite el Valor Compra ->"))

descuento = valorCompra * 0.15

precioFinal = valorCompra - descuento

print(f"El precio final a pagar es de ${precioFinal:.2f}")