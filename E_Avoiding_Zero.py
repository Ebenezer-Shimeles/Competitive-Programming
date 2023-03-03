t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    s = sum(nums)

    if s == 0:
        print('NO')
    elif s > 0:
        print('YES')
        nums.sort(reverse=True)
        print(*nums)
    elif s < 0:
        print('YES')
        nums.sort()
        print(*nums)  
        