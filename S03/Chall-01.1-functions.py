# CHALLENGE: FUNCTIONS
# crear una función que devuelva el cubo de una lista de números
numsOne = [ 2, 3, 5, 7, 6, 9 ]
numsTwo = [ 2, 1, 4, 12, 7 ]
def cubes( n ):
    cubesArray = []
    for x in n:
        cubesArray.append( x * x * x )
    return cubesArray

print(cubes( numsOne ))
print(cubes( numsTwo ))
