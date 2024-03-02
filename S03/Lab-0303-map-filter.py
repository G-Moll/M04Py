# Functions: Map, Filter, Reduce
# Map: APLICA UNA FUNCIÓN A CADA ÍNDICE DE UN ARREGLO
numsOne = [ 2, 3, 5, 7, 6, 9 ]
# def cubes( n ):
#     return n * n * n

# numCubes = map( cubes, numsOne )
# print( list( numCubes ) )

# Filter: APLICA UNA FUNCIÓN A CADA ÍNDICE DE UN ARREGLO, PARA FILTRAR LOS ÍNDICES QUE PASEN UNA EVALUACIÓN
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

# Reduce: APLICA UNA FUNCIÓN A CADA ÍNDICE DE UN ARREGLO, PARA GENERAR UN RESULTADO ÚNICO
import functools

print( "Sum All Array Numbers:", git functools.reduce( lambda a, b: a + b, numsTwo ) )
print( "Multiply All Array Numbers:", functools.reduce( lambda x, y: x * y, [ 1, 2, 3, 4 ] ) )
