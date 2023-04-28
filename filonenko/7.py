a = []
n = int( input() )
for i in range( 0, n ):
    b = int( input() )
    if b < 10:
        a.append(b)
    else:
        continue
print( sum( a ) )
