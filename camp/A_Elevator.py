t = int(input())

for _ in range(t):
    wt,et, ef = map(int, input().split())
    # et = int(input())
    # ef = int(input())
    # M = float('inf')
    # for n in range(5):
    #     k = (ef-n)*et
    
    #     t = n*wt + (4-n)*et + (k if k >=0 else 0)
    #     M = min(M, t)
    # print(M)
    total = 0
    for n in range(5):
        if et * (ef-n+1) <= wt:
            total += et
        else:
            total += wt
    print(total)