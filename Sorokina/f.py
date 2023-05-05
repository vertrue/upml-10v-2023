def v5(n, a):
    summa = 0;
    for i in range(n):
        if a[i]%2==0:
            summa += a[i]
    return summa 
