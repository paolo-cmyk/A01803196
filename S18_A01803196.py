temperaturas = [22, 25, 20, 30, 28, 18, 24]

promedio = sum(temperaturas) / len(temperaturas)
print("Temperatura promedio:", promedio)

for i in range(len(temperaturas)):
    if temperaturas[i] > promedio:
        print("Día", i+1, "está arriba de la media")
    else:
        print("Día", i+1, "está abajo de la media")
        
alumnos = ["Paolo", "Maya", "Alessandro", "Alfonso", "Diego"]
calificaciones = [75, 40, 90, 55, 100]


promedio = sum(calificaciones) / len(calificaciones)
print("Calificación promedio:", promedio)


for i in range(len(alumnos)):
    if calificaciones[i] < 60:
        print(alumnos[i], "reprobó")


aprobados = 0
for i in range(len(calificaciones)):
    if calificaciones[i] >= 60:
        aprobados += 1

porcentaje = (aprobados / len(alumnos)) * 100
print("Porcentaje de alumnos que pasaron:", porcentaje, "%")

compras = ["Leche", "Pan", "Huevos", "Manzanas"]
ya_comprado = [False, False, False, False]


for i in range(len(compras)):
    if not ya_comprado[i]:  # Solo los que no se han comprado
        respuesta = input(f"¿Ya compraste {compras[i]}? (s/n): ")
        if respuesta.lower() == "s":
            ya_comprado[i] = True

print("\nEstado de la lista de compras:")
for i in range(len(compras)):
    estado = " Comprado" if ya_comprado[i] else " Pendiente"
    print(f"{compras[i]} - {estado}")

    numeros = [15, 3, 28, 7, 10, 50, 2]

print("Valor máximo de la lista:", max(numeros))
print("Valor mínimo de la lista:", min(numeros))

ordenados = sorted(numeros)
print("Lista en orden:", ordenados)

enteros = [12, 7, 9, 20, 33, 14, 5]

pares = []
impares = []

for i in range(len(enteros)):
    if enteros[i] % 2 == 0:
        pares.append(enteros[i])
    else:
        impares.append(enteros[i])

print("Lista de pares:", pares)
print("Lista de impares:", impares)

usuarios = ["Paolo", "Maya", "Alessandro", "Diego"]

nuevo = input("Ingresa un nombre de usuario: ")

while nuevo in usuarios:
    print("Ese nombre ya existe, intenta con otro.")
    nuevo = input("Ingresa un nombre de usuario: ")

usuarios.append(nuevo)
print("Lista de usuarios actualizada:", usuarios)