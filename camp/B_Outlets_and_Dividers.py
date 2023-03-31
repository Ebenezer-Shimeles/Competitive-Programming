t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    if n <= 2:
        print('0')
    elif sum(a) - m + 2 < n:
        print(-1)
    else:
        i = 0
        s = 2
       
        while s < n:
          
            s += a[i]
            s -= 1
            i += 1
        print(i)
