# CHALLENGE: FUNCTIONS
# crear una función que devuelva el cubo de una lista de números
nums = [ 2, 3, 5, 7, 6, 9 ]
nums2 = [ 2, 1, 4, 12, 7 ]
def cubes( n ):
    cubesArray = []
    for x in n:
        cubesArray.append( x * x * x )
    return cubesArray

print(cubes( nums ))
print(cubes( nums2 ))
