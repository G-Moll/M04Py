# 0601 SENTENCIAS CONDICIONALES

# Ejercicio 0601 (1.5 puntos)
#     - Realizar un ejemplo de menú,
#         - donde podemos escoger las distintas opciones
#         - hasta que seleccionamos la opción de “Salir”.


menuOptions = [ "Exit", "Coffee", "Milk", "Orange Juice", "Scrambled Eggs", "Chilaquiles", "Sandwich", "Bread", "Hot Cakes", "Dessert" ]
choices = []


print("""
Please choose some (numeric) option:
    1) Coffee           4) Scrambled Eggs       7) Bread
    2) Milk             5) Chilaquiles          8) Hot Cakes
    3) Orange Juice     6) Sandwich             9) Dessert

    0) Exit Menu
""")

while True:
    inputChoice = int( input( "Please choose an option: " ) )

    if inputChoice == 0:
        break
    elif inputChoice == 1:
        choices.append( menuOptions[ 1 ] )
    elif inputChoice == 2:
        choices.append( menuOptions[ 2 ] )
    elif inputChoice == 3:
        choices.append( menuOptions[ 3 ] )
    elif inputChoice == 4:
        choices.append( menuOptions[ 4 ] )
    elif inputChoice == 5:
        choices.append( menuOptions[ 5 ] )
    elif inputChoice == 6:
        choices.append( menuOptions[ 6 ] )
    elif inputChoice == 7:
        choices.append( menuOptions[ 7 ] )
    elif inputChoice == 8:
        choices.append( menuOptions[ 8 ] )
    elif inputChoice == 9:
        choices.append( menuOptions[ 9 ] )

print( "Your breakfash choices: ", choices )
