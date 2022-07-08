# Programa 6

lista = []

cant_palabras = int(input("¿Cuantas palabras se agregaran a la lista?\n"))

for x in range(cant_palabras):

    palabra = input("Ingrese una palabra:\n")

    lista.append(palabra)

opcion = "z"

while opcion != "e" and len(lista) != 0:

    opcion = input("""
Ingrese la opcion a realizar:

a. Contar.
b. Modificar.
c. Eliminar.
d. Mostrar.
e. Terminar.\n""").lower()

    if opcion == "a":

        palabra = input("Ingrese una palabra para contar las veces que aparece en la lista:\n")

        contador = 0

        for i in lista:

            if palabra.lower() == i.lower():
                
                contador += 1
        

        if contador == 0:
            print(f"La palabra {palabra}, no aparece en la lista.")

        elif contador == 1:

            print(f"La palabra {palabra}, aparece 1 vez en la lista.")

        else:
            print(f"La palabra {palabra}, aparece {contador} veces en la lista.")
            
        
    elif opcion == "b":
        
        palabra_a_remplazar = input("Ingrese la palabra a remplazar:\n")

        palabra_remplazo = input("Ingrese la palabra nueva:\n")

        contador = 0

        for x in range(len(lista)):

            if lista[x].lower() == palabra_a_remplazar.lower():
                
                contador += 1
                
                lista.insert(x, palabra_remplazo)
                lista.pop(x + 1)
        
        if contador == 0:

            print(f"No se encontro la palabra '{palabra_a_remplazar}'")

        else:

            print(f"Se remplazo la palabra '{palabra_a_remplazar}' por '{palabra_remplazo}' en la lista.")

    elif opcion == "c":

        palabra = input("Ingrese la palabra a eliminar:\n")

        if palabra in lista:

            lista.remove(palabra)
            
            print(f"Se elimino la palabra '{palabra}' de la lista.")

        else:
            
            print(f"No se encontro la palabra {palabra} en la lista.")
    
    elif opcion == "d":

        print(f"La lista de palabras es:\n{lista}")

    elif opcion == "e":

        print("Programa terminado.")
    
    if len(lista) == 0:

        print("La lista ya no tiene palabras, el programa se termino.")
    
    print("------------------------------------------------------")
