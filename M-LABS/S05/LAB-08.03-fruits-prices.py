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
fruitsData[ "apple" ] = 40
fruitsData[ "banana" ] = 20
fruitsData[ "blueberry" ] = 30
fruitsData[ "cherry" ] = 50
fruitsData[ "kiwi" ] = 40
fruitsData[ "mango" ] = 25
fruitsData[ "melon" ] = 20
fruitsData[ "orange" ] = 20
fruitsData[ "strawberry" ] = 30
fruitsData[ "tangerine" ] = 25
fruitsData[ "watermelon" ] = 25

continueRequesting = True

while True:

    fruitName = str( input( "WHICH FRUIT WANNA REQUEST: " ) ).lower()
    fruitQuantity = int( input( "FRUIT SOLD QUANTITY: " ) )

    if fruitName not in fruitsData:
        print( "The requested fruit doesn't exist, please try again" )
        continue
    else:
        currentFruitName = fruitName
        currentFruitPrice = fruitsData[ fruitName ]
        currentFruitTotal = currentFruitPrice * fruitQuantity
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
