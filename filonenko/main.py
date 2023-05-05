from f import vv
    
a = []
n = int( input() )
for i in range( 0, n ):
    b = int( input() )
    if vv(b):
        a.append(b)
    else:
        continue

print( sum(a) )
