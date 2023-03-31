from math import floor
t = int(input())

for  _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    M = float('inf')
    if n <= 12:
        print(sum(w))
        break

    rest_len = n - ((n//6) * 6)
    
    if rest_len:
        rest = w[-rest_len:]
        M = min(M, sum(rest))
    
    prefs = []
    c, k = 0,0
    for i in range(n):
        c += w[i]
        k += 1

        if k == 6:
            prefs.append(c)
            c = 0
            k = 0
    # print(prefs)
    N = len(prefs)
    M = min(M, prefs[0]+prefs[1])
 
    c,k,start = 0,0, 2
        

    for i in range(2, len(prefs)): 
            c += prefs[i]
            k += 1
            if k == 2:
                M = min(M, c)
                c -= prefs[start]
                start += 1
                k -= 1
        



    


    print(M)
