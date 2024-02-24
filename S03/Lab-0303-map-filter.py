# Functions: Map, Filter
# Map
numsOne = [ 2, 3, 5, 7, 6, 9 ]
# def cubes( n ):
#     return n * n * n

# numCubes = map( cubes, numsOne )
# print( list( numCubes ) )

# Filter
numsTwo = [ 12, 7, 78, 2, 1, 4, 58, 38 ]
def gtX( n ):
    if n > 50:
        return True
    else:
        return False

filteredOnes = filter( gtX, numsOne )
print( list( filteredOnes ) )
filteredTwos = filter( gtX, numsTwo )
print( list( filteredTwos ) )
