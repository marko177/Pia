#Programa 3

dia = []
temperatura_min = []
temperatura_max = []
promedio = []

for x in range(5):

    nom = input("Ingrese el dia de la semana:\n")
    temp_min = int(input("Ingrese la temperatura minima de ese dia:\n"))
    temp_max = int(input("Ingrese la temperatura maxima de ese dia:\n"))

    dia.append(nom)
    temperatura_min.append(temp_min)
    temperatura_max.append(temp_max)

for x in range(5):

    prom_dia = round((temperatura_min[x] + temperatura_max[x]) / 2)
    promedio.append(prom_dia)

for x in range(5):
    
    print(f"El promedio de temperatura del dia {dia[x]} es: {promedio[x]}.")

for k in range(4):
    
    for x in range(4):

        aux_temp = promedio[x]
        aux_nom = dia[x]
        if promedio[x] > promedio[x + 1]:

            promedio[x] = promedio[x + 1]
            promedio[x + 1] = aux_temp

            dia[x] = dia[x + 1]
            dia[x + 1] = aux_nom

print(f"Los dias menos calurosos son:")

for x in range(2):
    
    print(f"Dia: {dia[x]}, Temperatura promedio: {promedio[x]}")
