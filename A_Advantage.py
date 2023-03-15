t = int(input())

for _ in range(t):
    n = int(input())
    st = list(map(int, input().split()))
 
    l = []
    m = sorted(st)
    i = 0
    j = n - 1
    #print(m)

    while i < n:
        if st[i] == m[j]:
           l.append(st[i] - m[j-1])
        
        else:
            l.append(st[i] - m[j])
        i += 1
    

  
    print(*l)