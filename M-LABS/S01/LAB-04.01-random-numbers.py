# 0401 TIPOS DE COLECCIÓN DE DATOS

# Ejercicio 0401 (1.2 puntos)
#     - Realizar un programa que inicialice una lista
#     - con 10 valores aleatorios (del 1 al 10)
#     - y posteriormente muestre en pantalla cada elemento de la lista
#         - junto con su cuadrado
#         - y su cubo.


import random

# listNumbers = [ 10, 15, 30, 12, 33, 7, 3, 8, 22, 1 ]
listNumbers = [ ]
for x in range(1, 11):
    randomNumber = random.randint( 1, 10 )
    listNumbers.append( randomNumber )
    print( "Number: ", randomNumber, ",\tSquare Number: ", randomNumber * randomNumber, ",\tCubic Number: ", randomNumber * randomNumber * randomNumber )

print( "\nAll numbers: ", listNumbers )
