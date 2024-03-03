# OOP Paradigma
class Student():
    # public, private, protected
    __name: str
    age: int
    single: bool

    @property
    def name( self ):
        return self.__name

    @name.setter
    def name( self, name ):
        self.__name = name

    # def __init__( self, n = "a", a = 10, s = False ):
    #     pass

    def __init__( self, n, a, s ):
        self.__name = n
        self.age = a
        self.single = s

    def hello( self ):
        print( "Hello", self.__name )

s1 = Student( "Bruno", 33, True )
s1.name = "Bruno Mars"
print( s1, s1.name, s1.age, s1.single )
# s1.hello()
# s2 = Student( "Angelica", 17, True )
# print( s2, s2.name, s2.age, s2.single )
# s2.hello()
# # # { name : "Bruno"
# # age : 33
# single : True}

# { name = "Angelica"
# age = 17
# single = True}


