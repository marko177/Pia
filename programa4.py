#Programa 4

nombres = []

total_kms = []

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
cant_conductores = int(input("Ingrese la cantidad de conductores en la empresa:\n"))

for x in range(cant_conductores):

    nom = input("Ingrese el nombre del conductor:\n")

    nombres.append(nom)
    
    km_por_dia = []

    for d in range(7):
        
        km = int(input(f"Ingrese los km's conducidos el dia {dias[d].lower()}:\n"))
        km_por_dia.append(km)

    suma = 0

    for k in km_por_dia:
        suma += k

    total_kms.append(suma)

print("Conductores y su total de km manejados:")

for x in range(len(nombres)):

    print(f"Conductor: {nombres[x]}, Total km: {total_kms[x]}")