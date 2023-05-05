import math
T = int(input())

def is_perfect(N):
    s= math.sqrt(N)
    return math.ceil(s) == math.floor(s)
for _ in range(T):
    print('-'*10)
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    r = N-1
    ans = 0
    while r >=2:
        l = 0
        while l < N-2:
            b = a[r]/a[l]

            if is_perfect(b):
                #print(f'{b} is perfect')
                b = int(b)
                mid = l+1
                while mid < N-1:
                   # print(f'Checking {a[l]} * {math.sqrt(b)} =={a[mid]} an')
                    if a[l]*math.sqrt(b) ==a[mid]:
                        ans += 1
                        break #to avoid over counting
                    mid += 1
            l += 1
        r -=1
    print(ans)

