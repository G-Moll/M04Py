# 0701 PROGRAMACIÓN ORIENTADA A OBJETOS

# Ejercicio 0701 (2 puntos)
#     - Vamos a crear una clase llamada Persona.
#         - Sus atributos son:
#             - nombre,
#             - edad
#             - y DNI.
#         - Construye los siguientes métodos para la clase:
#             - Un constructor, donde los datos pueden estar vacíos.
#             - Los setters y getters para cada uno de los atributos.
#             - Hay que validar las entradas de datos.
#             - mostrar():
#                 - Muestra los datos de la persona.
#             - esMayorDeEdad():
#                 - Devuelve un valor lógico indicando si es mayor de edad


class Person:

    __name: str
    __age: int
    __dni: str

    def __init__( self ):
        pass
        print( "Person Object Created" )
    # ·························
    def show( self ):
        try:
            return "\n\tname: " + self.name + "\n\tage: " + str( self.age ) + ",\n\tdni: " + self.dni
        except:
            print( "\t> EXCEPTION show() method: One or more Attributes are not defined" )
    # ·························
    def isLegalAge( self ):
        try:
            return self.age >= 18
        except:
            print( "\t> EXCEPTION isLegalAge() method: Attribute \"age\" is not defined" )
    # ·························
    @property
    def name( self ):
        try:
            if not self.__name:
                raise AttributeError
            else:
                # print(  "Person Name has been got: ", self.__name )
                return self.__name
        except AttributeError:
            print( "\t> EXCEPTION name getter: Attribute \"name\" is not defined" )

    @name.setter
    def name( self, name ):
        try:
            if not name or len( name ) <= 0:
                raise AttributeError
            else:
                self.__name = name
                print(  "Person Name has been set: ", self.name )
        except AttributeError:
            print( "\t> EXCEPTION name setter: Invalid value for \"name\" attribute" )
    # ·························
    @property
    def age( self ):
        try:
            if not self.__age:
                raise AttributeError
            else:
                # print(  "Person Age has been got: ", self.__age )
                return self.__age
        except:
            print( "\t> EXCEPTION age getter: Attribute \"age\" is not defined" )

    @age.setter
    def age( self, age ):
        try:
            if not age or age <= 0:
                raise AttributeError
            else:
                self.__age = age
                print(  "Person Age has been set: ", self.age )
        except AttributeError:
            print( "\t> EXCEPTION age setter: Invalid value for \"age\" attribute" )
    # ·························
    @property
    def dni( self ):
        try:
            if not self.__dni:
                raise AttributeError
            else:
                # print(  "Person DNI has been got: ", self.__dni )
                return self.__dni
        except:
            print( "\t> EXCEPTION dni getter: Attribute \"dni\" is not defined" )

    @dni.setter
    def dni( self, dni ):
        try:
            if not dni or len( dni ) < 0:
                raise AttributeError
            else:
                self.__dni = dni
                print(  "Person DNI has been set: ", self.dni )
        except AttributeError:
            print( "\t> EXCEPTION dni setter: Invalid value for \"dni\" attribute" )
    # ·························

# ································································
# print( "\n································································" )
# print( "\n::: CREATING PERSON ONE" )
# person = Person()

# print( "\n::: SETTERS FOR PERSON ONE" )
# person.name = "Jesús"
# person.age = 33
# person.dni = "JHS137"

# print( "\n::: GETTERS FOR PERSON ONE" )
# print( "person.name: ", person.name )
# print( "person.age: ", person.age )
# print( "person.dni: ", person.dni )


# print( "Person Show: ", person.show() )
# print( "Person Legal Age:\n\tLegal Age: ", person.isLegalAge(), "\n\tPerson Age: ", person.age )


# ········································································
# print( "\n········································································" )
# print( "\n::: CREATING PERSON TWO" )
# personTwo = Person()
# print( "personTwo: ", personTwo )

# print( "\n::: EXCEPTION HANDLING ON SETTERS" )
# personTwo.name = 0
# personTwo.age = 0
# personTwo.dni = ""

# print( "\n::: EXCEPTION HANDLING ON GETTERS" )

# print( "person.name: ", personTwo.name )
# print( "person.age: ", personTwo.age )
# print( "person.dni: ", personTwo.dni )

# print( "\n::: EXCEPTION HANDLING ON INSTANCE METHODS" )
# personTwo.show()
# personTwo.isLegalAge()
