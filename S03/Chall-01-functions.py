# CHALLENGE: FUNCTIONS
# crear una función que devuelva el cubo de una lista de números
nums = [ 2,5,7, 6, 9 ]
def cubes( n ):
    cubesArray = []
    for x in n:
        cubesArray.append( x * x * x )
    return cubesArray

print(cubes( nums ))
