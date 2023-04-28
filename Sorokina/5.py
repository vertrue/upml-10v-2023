n = int(input())

a = []
for i in range(n):
    el = int(input())
    a.append(el)

summa = 0;
for i in range(n):
    if a[i]%2==0:
        summa += a[i]

print(summa)        
    
