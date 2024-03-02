# OOP Paradigma
class Student():
    name: str
    age: int
    single: bool

    # def __init__( self, n = "a", a = 10, s = False ):
    #     pass

    def __init__( self, n, a, s ):
        self.name = n
        self.age = a
        self.single = s

    def hello( self ):
        print( "Hello", self.name )

s1 = Student( "Bruno", 33, True )
print( s1, s1.name, s1.age, s1.single )
s1.hello()
s2 = Student( "Angelica", 17, True )
print( s2, s2.name, s2.age, s2.single )
s2.hello()
# # { name : "Bruno"
# age : 33
# single : True}

# { name = "Angelica"
# age = 17
# single = True}


