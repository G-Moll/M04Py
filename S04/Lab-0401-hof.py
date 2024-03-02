# HOF High Order Functions
def outer( fn ):
    fn()
def hello():
    print( "Hello "*3 )
def bye():
    print( "Bye "*3 )
outer( hello )
outer( bye )

def outerBis( arr ):
    arr[ 0 ]()
    arr[ 1 ]()
outerBis( [ hello, bye ] )

