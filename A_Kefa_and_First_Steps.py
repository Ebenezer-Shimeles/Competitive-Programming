N = int(input())
a = list(map(int, input().split()))

m = 1

c = 1
i = 0

while i < N:
    j = i + 1
    while j < N:
        if a[j-1] <= a[j]:
            c += 1
            j+= 1 
        else:
            m = max(m, c)
            c = 1
            break
    m = max(m, c)
    i = j
   
print(m)