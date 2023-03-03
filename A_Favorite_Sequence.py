t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    i = 0
    j = n - 1
    ret = []
    while  i < j:
        ret.append(nums[i])
        ret.append(nums[j])
        i += 1
        j -=1
    if n % 2:
        ret.append(nums[i])
    print(*ret)
