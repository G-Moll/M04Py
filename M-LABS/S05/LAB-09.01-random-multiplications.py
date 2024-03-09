# 0901 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0901 (1.5 puntos)
#     - Realice un programa que pregunte aleatoriamente una multiplicación.
#         - El programa debe indicar
#             - si la respuesta ha sido correcta o no
#             - (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta).

#     # El programa preguntará 10 multiplicaciones,
#     # y al finalizar mostrará el número de aciertos.


import random

userResults = { "right": 0, "wrong": 0 }

def randomMultiplication():
    attempt = {}
    attempt[ "numOne" ] = random.randint( 1, 10 )
    attempt[ "numTwo" ] = random.randint( 1, 10 )
    attempt[ "multNumbers" ] = attempt[ "numOne" ] * attempt[ "numTwo" ]
    return attempt

def promptUser():
    num = 1
    while num <= 10:
        currentMultiplication = randomMultiplication()
        numOne = currentMultiplication[ "numOne" ]
        numTwo = currentMultiplication[ "numTwo" ]
        multNumbers = currentMultiplication[ "multNumbers" ]


        userAnswer = int(input( "What is the result of multiplication using " + str(numOne) + " and " + str( numTwo ) + ": " ))

        if userAnswer != multNumbers:
            userResults[ "wrong" ] += 1
        else:
            userResults[ "right" ] += 1

        num += 1

    return "Completed"

def showResults():
    return "RIGHT ANSWERS: " + str( userResults[ "right" ] ) + "\nWRONG ANSWERS: " + str( userResults[ "wrong" ] )


promptUser()
print( showResults() )
