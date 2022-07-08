
#Programa 2

# 2. Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
#   a.	Todos los alumnos mayores de edad.




nombres = []
edades = []

nom = ""

while nom != "*":
    
    nom = input("Ingrese el nombre del alumno (* para terminar):\n")
    if nom != "*":
        edad = int(input("Ingrese la edad del alumno en años cumplidos:\n"))
    else:
        pass
    nombres.append(nom)
    edades.append(edad)

print("Alumnos mayores de edad:\n")

for x in range(len(nombres) - 1):

    if edades[x] >= 18:
        print(f"Nombre: {nombres[x]}, Edad: {edades[x]}")
