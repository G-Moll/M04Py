# 0903 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0903 (1.5 puntos)
#     - Obtener la cantidad de elementos mayores a 5 en la tupla.
#     # tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)



tupleData = ( 5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3 )
numberEdge = 5

def getUpperNumbers( tupleData ):
    chosenNumbers = []
    for n in tupleData:
        if n > numberEdge:
            chosenNumbers.append( n )

    return chosenNumbers

filteredNumbers = getUpperNumbers( tupleData )
print( "NUMBERS GREATER THAN " + str( numberEdge ), "\nTotal Numbers: ", len( filteredNumbers ), "\nFiltered Numbers: ", filteredNumbers )
