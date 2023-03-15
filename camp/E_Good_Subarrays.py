from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, list(input())))
   
  
    s = sum(a)
    c = 0

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s == j-i +1:
                c += 1


   


   


    print(c)

             