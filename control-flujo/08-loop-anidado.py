'''
LOOP ANIDADO
           
           Explicacion del Ejemplo
           
           j=0
           k=0
           j=0 la segunda vez no se ejecuta
           k=1 la segunda vez si se ejecuta
           j=1
           k=1
           j=2
           k=0
           j=2
           k=1
                     
           
'''
#Tienen un fin exclusivo los for aninados, 
for j in range(3): #Outer for/loop
    for k in range(2): #Inner for/loop
        print(f"{j}, {k}")