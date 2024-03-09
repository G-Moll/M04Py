# 0803 MÉTODOS DE LOS OBJETOS

# Ejercicio 0803 (2 puntos)
#     - Vamos a crear un programa en Python donde vamos a declarar
#         - un diccionario para guardar
#         - los precios de las distintas frutas.

#     # El programa pedirá
#         # el nombre de la fruta
#         # y la cantidad que se ha vendido
#         # y nos mostrará el precio final de la fruta
#             # a partir de los datos guardados en el diccionario.
#         # Si la fruta no existe nos dará un error.
#         # Tras cada consulta
#             # el programa nos preguntará si queremos hacer otra consulta.



fruitsData = {}
fruitsData[ "apple" ] = { "price" : 40, "sold": 0 }
fruitsData[ "banana" ] = { "price" : 20, "sold": 0 }
fruitsData[ "blueberry" ] = { "price" : 30, "sold": 0 }
fruitsData[ "cherry" ] = { "price" : 50, "sold": 0 }
fruitsData[ "kiwi" ] = { "price" : 40, "sold": 0 }
fruitsData[ "mango" ] = { "price" : 25, "sold": 0 }
fruitsData[ "melon" ] = { "price" : 20, "sold": 0 }
fruitsData[ "orange" ] = { "price" : 20, "sold": 0 }
fruitsData[ "strawberry" ] = { "price" : 30, "sold": 0 }
fruitsData[ "tangerine" ] = { "price" : 25, "sold": 0 }
fruitsData[ "watermelon" ] = { "price" : 25, "sold": 0 }


# def fruitExists( fruitRequested ):
#     if not fruitsData[ fruitRequested ]:
#         return False
#     else:
#         return fruitsData[ fruitRequested ]

# print( not fruitsData[ "watermelon" ] )
# print( fruitsData )

continueRequesting = True

while True:

    fruitName = str( input( "WHICH FRUIT WANNA REQUEST: " ) )
    fruitQuantity = int( input( "FRUIT SOLD QUANTITY: " ) )

    if not fruitsData[ fruitName ]:
        print( "The requested fruit doesn't exist, please try again" )
        continue
    else:
        currentFruitName = fruitName
        currentFruitPrice = fruitsData[ fruitName ][ "price" ]
        currentFruitTotal = currentFruitPrice * fruitQuantity
        # "${:,.2f}".format( currentFruitPrice )
        # "${:,.2f}".format( currentFruitTotal )
        print( "FRUIT: ", currentFruitName,"\tPRICE: ", "${:,.2f}".format( currentFruitPrice ), "\tSOLD: ", fruitQuantity, "\tTOTAL", "${:,.2f}".format( currentFruitTotal ) )

    new_request_message = """
    DO YO WANT TO REQUEST AGAIN?
    Type 0 (Zero) to termiante
    Type a different value to 0 (Zero) to continue
    """
    new_request = input( new_request_message )
    if int(new_request) == 0:
        print( "Thanks for requesting..!" )
        break
    else:
        continue
