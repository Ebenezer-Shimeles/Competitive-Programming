t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    i = 0
    removed = 0
    while i < n - 1:
        if nums[i+1] - nums[i] <= 1: 
            removed += 1
        i += 1


    if n - removed == 1:
        print("YES")
    else:
        print("NO")