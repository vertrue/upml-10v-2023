n = int(input())
a = [int(input()) for i in range(n)]
b = 0
for i in range(n):
    if a[i] == 0:
        b += 2
print(b)
