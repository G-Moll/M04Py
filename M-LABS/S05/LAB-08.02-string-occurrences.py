# 0802 MÉTODOS DE LOS OBJETOS

# Ejercicio 0802 (2 puntos)
#     - Escribe un programa
#         - que lea una cadena
#         - y devuelva un diccionario
#             - con la cantidad de apariciones
#             - de cada carácter en la cadena.


inputString = """
Icing apple pie topping gummies biscuit chocolate pastry marshmallow sesame snaps. Jujubes halvah soufflé brownie cookie liquorice gingerbread chocolate bar chupa chups. Jelly-o macaroon carrot cake cotton candy toffee gummi bears powder brownie danish. Powder cake macaroon marshmallow cupcake chocolate bar macaroon halvah.

Tart bear claw toffee chocolate bar carrot cake pastry jelly-o. Bonbon toffee gummies croissant liquorice cookie cheesecake toffee cookie. Jelly beans danish croissant sesame snaps jujubes. Cake pie pastry jujubes cheesecake powder powder tart cake.

Dragée jelly beans liquorice soufflé cake brownie cotton candy. Pie marzipan sesame snaps cake oat cake carrot cake donut. Apple pie bear claw tart chocolate chocolate bar candy canes powder.

Danish apple pie donut bear claw lollipop tiramisu muffin. Apple pie marshmallow cake cookie chupa chups bonbon danish jelly pie. Cupcake dessert sweet roll gummi bears croissant sesame snaps. Bonbon cookie chocolate pudding liquorice croissant gummies wafer sweet roll.

Bonbon chocolate carrot cake sugar plum apple pie. Cookie marshmallow donut pastry chocolate cake. Marzipan chocolate bar cheesecake pudding marzipan.


Cupcake ipsum dolor sit amet. Ice cream toffee macaroon sugar plum toffee I love cake. Pastry gummies powder dragée candy canes bonbon biscuit. Liquorice pudding chupa chups caramels bear claw chocolate ice cream.

Oat cake cheesecake tiramisu bonbon fruitcake topping gingerbread. Soufflé donut lollipop brownie jelly-o dragée bonbon dessert. Fruitcake candy canes I love sesame snaps dragée wafer pie cake. Chupa chups toffee cotton candy gummies pudding ice cream candy canes cupcake icing.

Cheesecake apple pie muffin gummi bears I love. Ice cream candy canes donut bear claw soufflé sweet pudding marzipan. I love halvah chocolate icing pie soufflé gingerbread. Ice cream powder halvah bonbon dessert gummi bears sweet tiramisu sesame snaps.

I love cake I love gummi bears powder jelly-o cupcake. Toffee marzipan dessert muffin cake jelly. Cheesecake gummies topping candy canes carrot cake sugar plum sesame snaps fruitcake.

Pie cheesecake dragée I love lemon drops. Halvah candy canes I love marzipan icing. Croissant pie cupcake cake jujubes oat cake cake. Gummi bears danish chupa chups pudding cupcake pie candy canes donut brownie.
"""
inputString = str( input( "Type some text in order to count its characters: " ) )
countedChars = {}

for s in range( len( inputString ) ):
    if not countedChars.get( inputString[ s ] ):
        countedChars.update( { inputString[ s ] : 1 } )
    else:
        currentKey = inputString[ s ]
        updatedValue = countedChars.get( currentKey ) + 1
        countedChars[ currentKey ] = updatedValue

# countedChars[ "Jesús" ] = 371
# print( countedChars.get( "Jesús" ) )
# print( countedChars.get( "Jesús", 317 ) )
# print( countedChars.get( "One" ) )
print( "\nINPUT TEXT:\n", inputString )
print( "\nTOTAL CHARACTERS:\n", len( countedChars.items() ), countedChars.keys() )
print( "\nALL CHARACTERS:\n", countedChars )
print( "\nALPHABETIC ORDER:\n", dict( sorted( countedChars.items() ) ) )
print( "\nOCCURRENCE ORDER:\n", dict( sorted( countedChars.items(), key=lambda item: item[ 1 ], reverse = True ) ) )
