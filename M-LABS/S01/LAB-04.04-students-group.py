# 0404 TIPOS DE COLECCIÓN DE DATOS

# Ejercicio 0404 (1.2 puntos)
#     - Codifica un programa en Python que nos permita
#         - guardar los nombres de los alumnos de una clase
#         - y las notas que han obtenido.
#     - Cada alumno puede tener distinta cantidad de notas.
#     - Guarda la información en un diccionario
#         - cuya claves serán los nombres de los alumnos
#         - y los valores serán listados con las notas de cada alumno.

#     - El programa pedirá el número de alumnos que vamos a introducir,
#         - pedirá su nombre
#         - e irá pidiendo sus notas
#         - hasta que introduzcamos un número negativo.
#     - Al final el programa nos mostrará
#         - la lista de alumnos
#         - y la nota media obtenida por cada uno de ellos.

#     - Nota: si se introduce el nombre de un alumno que ya existe
#         - el programa nos dará un error.


studentsGroup = {}
studentsQuantity = int( input( "How many students will be stored: " ) )

for student in range( studentsQuantity ):
    currentStudentName = input( "Student " + str( student + 1 ) + " Name: " )
    currentStudentNotes = []
    studentsGroup[ currentStudentName ] = []
    # print( currentStudentName )
    while True:
        currentNote = float( input( "\tNew Note for " + currentStudentName + ": " ) )
        if currentNote > 10:
            currentNote = 10
        elif currentNote < 0:
            break
        currentStudentNotes.append( currentNote )

    studentsGroup[ currentStudentName ] = currentStudentNotes


print( "\nINDIVIDUAL STUDENT RESULTS:" )
for currentStudent in studentsGroup:
    currentData = studentsGroup[ currentStudent ]
    currentQuantityNotes = len( currentData )
    print( "\tName:", currentStudent, "\tQuantity Notes:", currentQuantityNotes, "\tAverage: ", sum( currentData ) / currentQuantityNotes, "\tAll Notes:", currentData )


print( "\nALL GROUP DATA:\n\t", studentsGroup )
