#Ejemplo

usuarios = [
    ["David", 3],
    ["Aliset", 1],
    ["Pulga", 5],
]

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

#En una sola linea todo el codigo anterior
nombres = [usuario[0] for item in usuarios]
print(nombres)
