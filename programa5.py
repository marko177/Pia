# Programa 5

lista = []

opcion = "z"

while opcion != "i":

    opcion = input("""
Ingrese la opcion a realizar:

a. Añadir número a la lista.
b. Añadir número de la lista en una posición.
c. Longitud de la lista.
d. Eliminar el último número.
e. Eliminar un número.
f. Contar números.
g. Posiciones de un número.
h. Mostrar números.
i. Salir\n""")

    if opcion == "a":

        num = int(input("Ingrese el numero a añadir:\n"))
        lista.append(num)
        print(f"Se agrego el numero '{num}' a la lista.")

    elif opcion == "b":
        
        if len(lista) > 0:

            num = int(input("Ingrese el numero a añadir:\n"))
            pos = int(input(f"Ingrese la posision del numero (Maximo {len(lista) - 1}):"))

            lista.insert(pos, num)

            print(f"Se agrego el numero '{num}' a la lista.")

    elif opcion == "c":
        
        print(f"Longitud de la lista: {len(lista)}.")

    elif opcion == "d":
        
        print(f"Se removio el ultimo numero ('{lista[-1]}') de la lista.")

        lista.pop(-1)

        
    elif opcion == "e":

        num = int(input("Ingrese el numero a remover:\n"))
        
        if num in lista:
            lista.remove(num)
            print(f"Se removio el numero '{num}' de la lista.")
        
        else:
            print(f"El numero '{num}' no esta en la lista.")
            
    elif opcion == "f":
        
        cant = 0

        num = int(input("Ingrese el numero a revisar:\n"))

        for i in lista:

            if num == i:

                cant += 1

        if cant == 0:
            print("El numero '{num}' no aparece en la lista.")
        
        elif cant == 1:
            print(f"El numero '{num}' aparece 1 vez en la lista.")
        
        else:
            print(f"El numero '{num}' aparece {cant} veces en la lista.")
        
    elif opcion == "g":

        num = int(input("Ingrese el numero a revisar:\n"))
        
        pos_lista = []

        pos = 1
         
        for i in lista:

            if num == i:

                pos_lista.append(pos)
            
            pos += 1

        if len(pos_lista) == 0:

            print("El numero '{num}' no aparece en la lista.")

        elif len(pos_lista) == 1:
            
            print(f"El numero '{num}' esta en la posicion:\n{pos_lista[0]}")

        else:
            
            print("El numero '{num}' esta en las posiciones:")

            for i in pos_lista:
                print(i)

    elif opcion == "h":

        print(f"La lista de numeros es:\n{lista}")
        pass    

    elif opcion == "i":
        
        print("Programa Terminado.")  
    print("------------------------------------------------------")