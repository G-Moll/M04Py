# 0603 SENTENCIAS CONDICIONALES

# Ejercicio 0603 (1.5 puntos)
#     - Una persona adquirió un producto para pagar en 20 meses.
#     - El primer mes pagó 10 €,
#     - el segundo 20 €,
#     - el tercero 40 €
#     - y así sucesivamente.
#         # Realizar un algoritmo para determinar
#         # cuánto debe pagar mensualmente
#         # y el total de lo que pagó después de los 20 meses.


basePayment = 10
currentPayment = 0
totalPayment = 0

for n in range( 1 , 21 ):
    if n == 1:
        currentPayment = basePayment
    else:
        currentPayment = currentPayment * 2

    totalPayment += currentPayment

    print( "Payment " , n, "\tAmmount ", "$ {:,}".format( currentPayment ) )

print( "\nTOTAL PAYMENT ", "$ {:,}".format( totalPayment ) )
