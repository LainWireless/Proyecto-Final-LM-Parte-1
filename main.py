import json
from funciones import *
ts="1"
key="7210c08a52ee690052f11798b7eed7b7"
khash="36c02d07d35c20e636ba041f9b6f210c"
print()
print('''1. Buscar información de un personaje a partir del nombre, se mostrarán todos los personajes que coincidan con ese nombre.
2. Mostrar informacion de las series de cómics existentes a partir del año y nombre de la serie.
3. Mostrar información de cómics en los que aparece un personaje mediante su ID.
4.Salir.
''')
opcion=int(input("Introduce una opcion: "))
while opcion != 4:
    if opcion == 1:
        print()
        print("---PERSONAJES---")
        print()
        nombre=(input("Introduce un nombre: "))
        print()
        personajes(ts, key, khash, nombre)
        print()
    if opcion == 2:
        print()
        print("---SERIES DE CÓMICS---")
        print()
        nombre=(input("Introduce un nombre: "))
        año=(input("Introduce un año: "))
        print()
        series(ts, key, khash, nombre, año)
        print()
    if opcion == 3:
        print()
        print("---CÓMICS---")
        print()
        id=(input("Introduce un ID: "))
        print()
        comics(ts, key, khash, id)
        print()
    print('''1. Buscar información de un personaje a partir del nombre, se mostrarán todos los personajes que coincidan con ese nombre.
2. Mostrar informacion de las series de cómics existentes a partir del año y nombre de la serie.
3. Mostrar información de cómics en los que aparece un personaje mediante su ID.
4.Salir.
''')
    opcion=int(input("Introduce una opcion: "))


    