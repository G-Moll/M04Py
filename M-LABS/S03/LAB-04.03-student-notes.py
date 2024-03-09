# 0403 TIPOS DE COLECCIÓN DE DATOS

# Ejercicio 0403 (1.2 puntos)
#     - Se quiere realizar un programa que lea por teclado
#         - las 5 notas obtenidas por un alumno
#         - (comprendidas entre 0 y 10).
#     - A continuación debe mostrar todas las notas,
#     - la nota media,
#     - la nota más alta que ha sacado y
#     - la menor.


studentNotes = []

while len( studentNotes ) < 5 :
    currentNote = float( input( "Type a student note: " ) )
    if currentNote > 10:
        currentNote = 10
    elif currentNote < 0:
        currentNote = 0
    studentNotes.append( currentNote )

print( "\nSTUDENT RESULTS " )
print( "Student notes: ", studentNotes )
print( "Average notes: ", sum( studentNotes ) / len( studentNotes ) )
print( "Maximun note: ", max( studentNotes ) )
print( "Minimun note: ", min( studentNotes ) )
