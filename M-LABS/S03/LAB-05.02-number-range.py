# 0502 OPERADORES RELACIONALES

# Ejercicio 0502 (2 puntos)
#     - Programa que imprima si el número ingresado esta en el rango de 1 a 7.


currentNumber = float( input( "Type a number between 1 and 7: " ) )

if currentNumber < 1 or currentNumber > 7:
    print( "CONGRATS: The typed number is out of range (between 1 and 7), ", currentNumber )
else:
    print( "OOPS: The typed number is inside range (between 1 and 7), ", currentNumber )
