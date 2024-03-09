# 0503 OPERADORES RELACIONALES

# Ejercicio 0503 (2 puntos)
#     -Programa que calcule el interés de una cantidad
#     - si es mayor al 30%,
#     - sino informa el importe total.


print( """
Formats numbers
- Quantity: \t33.50 \t10
- Interest: \t10.35 \t5
\n""" )

quantity = float( input( "Type the quantity: " ) )
interest = float( input( "Type the interest: " ) ) / 100
total = 0
if interest > 0.3:
    total = quantity + ( quantity * interest )
    print( "The total ammount is: ", total )
else:
    print( "The total ammount is: ", quantity )
