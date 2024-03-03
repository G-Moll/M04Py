# CHALLENGE: OOP
# Crear clases que representen un Curso y a alumnos
# Tengan propiedades y metodos

class Lesson():
    students: int

    def __init__( self, students ):
        self.students = students

    def start( self ):
        print( "starting lesson" )
    def conclude( self ):
        print( "concluding lesson" )

lesson = Lesson( 10 )
print( lesson.students )
lesson.start()
lesson.conclude()
