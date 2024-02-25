# CHALLENGE: FILTER
# De una lista de diccionarios, filtrar las personas que sean de CDMX y mayores de Edad

people = [
    { "name": "Alejandra", "age": 26, "city": "CDMX" },
    { "name": "Juan", "age": 46, "city": "CDMX" },
    { "name": "Alberto", "age": 16, "city": "CDMX" },
    { "name": "Peter", "age": 28, "city": "OAX" },
    { "name": "Mariana", "age": 28, "city": "PUE" }
]

def filterPeople( person ):
    if person[ "age" ] >= 18 and person[ "city" ] == "CDMX":
        return True
    else:
        return False

filteredPeople = filter( filterPeople, people )
listPeople = list( filteredPeople )
print( listPeople )

# Map message
def message( p ):
    return p[ 'name' ] + " puede votar"

messages = map( message, listPeople )
print( list( messages  ) )
# hola :)
