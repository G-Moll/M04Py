# OOP Classes
# Herencia
# Classes, Super Classes, Sub Classes
class Animal():
    def eat( self ):
        print( "Eating something" )

class Feline():
    def roar( self ):
        print( "Roaring" )

class Cat( Animal, Feline ):
    pass

c = Cat()
c.eat()
c.roar()
# a = Animal()
# print( a )
