# 0902 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0902 (1.5 puntos)
#     - Obtener el cuadrado de todos los elementos en la lista.

# Lista: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


def squareNumbers( baseNumbers ):
    squaredNumbers = []
    for n in baseNumbers:
        squaredNumbers.append( n * n )
    return squaredNumbers

baseNumbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


print( "Base Numbers:\t", baseNumbers )
print( "Squared Numbers:", squareNumbers( baseNumbers ) )
