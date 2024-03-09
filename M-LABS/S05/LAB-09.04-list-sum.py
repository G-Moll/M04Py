# 0904 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0904 (1.5 puntos)
#     - Obtener la suma de todos los elementos en la lista.



listNumbers = [ 10, 15, 20, 3, 15, 0.25, 3.7, 7.3 ]

def sumList( listNumbers ):
    listSum = 0
    for n in listNumbers:
        listSum += n
    return listSum

print( "Summing List Numbers using Py Method: ", sum( listNumbers ) )
print( "Summing List Numbers using Custom Method: ", sumList( listNumbers ) )
