# 0405 TIPOS DE COLECCIÓN DE DATOS

# Ejercicio 0405 (1.2 puntos)
#     - Crea una tupla con los meses del año,
#     - pide números al usuario,
#     - si el número está entre 1 y la longitud máxima de la tupla,
#         - muestra el contenido de esa posición
#         - sino muestra un mensaje de error.
#     - El programa termina cuando el usuario introduce un cero.

print( """
OPTION A: Type 0 number to EXIT
OPTION B: Type a number between 1 and 12 in order to choose a month
 1: Jan \t 2: Feb \t 3: Mar
 4: Apr \t 5: May \t 6: Jun
 7: Jul \t 8: Aug \t 9: Sep
10: Oct \t11: Nov \t12: Dec
\n
""" )


months = ( "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" )


while True:
    userOption = int( float( input( "Type a number: " ) ) )

    print( userOption )

    if userOption == 0:
        print( "See you soon..!" )
        break
    elif userOption < 1 or userOption > len( months ):
        print( "Your choise is out of range: 1 - 12, ( choice: ", userOption, " )" )
    else:
        print( months[ userOption - 1 ] )
