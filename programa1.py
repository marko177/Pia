#Programa 1

#1.	Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista3 = []

for i in range(5):

    num = int(input("Ingrese un numero entero para la lista 1:\n"))
    lista1.append(num)

for i in range(5):

    num = int(input("Ingrese un numero entero para la lista 2:\n"))
    lista2.append(num)

for i in lista1:
    lista3.append(i)

for i in lista2:
    lista3.append(i)

print(f"La lista 1 es:\n{lista1}")
print(f"La lista 2 es:\n{lista2}")
print(f"La lista 3 es:\n{lista3}")