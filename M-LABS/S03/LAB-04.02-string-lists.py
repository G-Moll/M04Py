# 0402 TIPOS DE COLECCIÓN DE DATOS

# Ejercicio 0402 (1.2 puntos)
#     - Crea una lista
#         - e inicializarla con 5 cadenas de caracteres
#         - leídas por teclado.
#     - Copia los elementos de la lista
#         - en otra lista pero en orden inverso,
#     - y muestra sus elementos por la pantalla.


userOptions = []
reverseOptions = []

while len( userOptions ) < 5:
    userInput = input( "Type a word: " )
    userOptions.append( userInput )
    reverseOptions.insert( 0, userInput )

print( "Options:\t", userOptions )
print( "Inverted:\t", reverseOptions )
