t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    pref = w.copy()

    for i in range(n - 1):
        pref[i+1] += pref[i]
    print(pref)
    if n < 12:
        print(pref[-1])
    
    m = float('inf')
    k = 0
    i = 0
    curr_sum = 0
    start = pref[0]
    while i < n:
        c = 0
        if i == 0:
           c = (pref[0])
        else:
           c = (pref[i-1])
        k += 1
        if i//6 == 2:
            m = min(m, c)
            print("dsdsd", m, i)
        elif i//6 == 3:
            m = min(m, c)
            k -= 1
            x = c - start 
            start = pref[i - 1]
            m = min(x, m)
        i += 6
       
    print(m)