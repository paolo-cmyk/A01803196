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