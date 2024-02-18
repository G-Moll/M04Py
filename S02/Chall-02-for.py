nums = [ 2, 5, 15, 21, 16, 18, 7, 8, 37, 33, 78, 82, 28, 25, 12, 40, 3, 20, 45, 55, 20, 21 ]

# 1) Con la lista de números, calcular el Cuadrado
print( '\n:::: LAB 01 - CUADRADOS ::::' )
for x in range( len( nums ) ):
    print( "Cuadrado de" , nums[ x ], "es", nums[ x ] * nums[ x ] )


# 2) Usando una lista de números, imprimir si es par o impar
print( '\n:::: LAB 02 - PARES IMPARES ::::' )
for x in range( len( nums ) ):
    if nums[ x ] % 2 == 0:
        print( nums[ x ], "es par" )
    else:
        print( nums[ x ], "es impar" )


# 3) Imprimir sólo los números donde su cubo sea mayor a 5000
print( '\n:::: LAB 03 - CUBOS MAYORES A 500 ::::' )
for x in range( len( nums ) ):
    cube = nums[ x ] * nums[ x ] * nums[ x ]
    if cube > 5000:
        print( "Número:", nums[ x ], ", cubo:", cube )


# 4) EXTRA: Calcular el promedio (Media) de los números
print( '\n:::: LAB 04 EXTRA - PROMEDIO DE NÚMEROS ::::' )
nums_count = len( nums )
nums_sum = 0
for x in range( nums_count ):
    nums_sum += nums[ x ]

print( "Cantidad de números", nums_count, ", Suma:", nums_sum, ", Promedio:", nums_sum / nums_count )
