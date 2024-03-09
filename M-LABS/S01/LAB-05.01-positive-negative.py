# 0501 OPERADORES RELACIONALES

# Ejercicio 0501 (2 puntos)
#     - Programa que imprima si el número es positivo o negativo.


currentNumber = float( input( "Type a number: " ) )

if currentNumber > 0:
    print( "The typed number is positive" )
elif currentNumber < 0:
    print( "The typed number is negative" )
else:
    print( "The typed number is neutro" )
