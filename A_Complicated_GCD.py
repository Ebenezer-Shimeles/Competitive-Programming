def GCD(a, b):

    if b == 0:
        return a
    return GCD(b, a%b)

a, b = map(int, input().split())

g =a
for i in range(a, b+1):
    g = GCD(i, g)
    if g == 1:
        break
   
print(g) 