# 0604 SENTENCIAS CONDICIONALES

# Ejercicio 0604 (1.5 puntos)
#     - Crea una aplicación que
#     - pida un número
#     - y calcule su factorial
#         # (El factorial de un número es el producto
#         # de todos los enteros entre 1 y el propio número
#         # y se representa por el número seguido de un signo de exclamación.
#         # Por ejemplo 5! = 1x2x3x4x5=120).


factorialInput = int( input( "Please type a interger number: " ) )
factorialResult = 0
currentCalculation = 1

if factorialInput > 0:
    for n in range( 1, factorialInput + 1 ):
        currentCalculation = currentCalculation * n
    print( "Factorial for number ", factorialInput ," is: ", "{:,}".format( currentCalculation ) )
else:
    print( "Factorial for Zero (0) number is: ", 1 )
