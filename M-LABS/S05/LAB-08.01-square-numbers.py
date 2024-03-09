# 0801 MÉTODOS DE LOS OBJETOS

# Ejercicio 0801 (2 puntos)
#     - Escribe un programa Python
#         - que pida un número por teclado
#         - y que cree un diccionario
#             - cuyas claves sean desde el número 1 hasta el número indicado,
#             - y los valores sean los cuadrados de las claves.


squaredNumbers = {}
limitKeys = int( input( "How many Square numbers will be calculated? " ) )
# limitKeys = 100

for t in range( 1, limitKeys + 1 ):
    # squaredNumbers[ t ] = t * t
    squaredNumbers[ t ] = pow( t, 2 )

print( "Squared Numbers: ", squaredNumbers )
