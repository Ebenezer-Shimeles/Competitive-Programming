t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    i = 0
    j = n - 1

    result = []
    
    b = 0
    while i <= j:
        if not b%2 :
            result.append(nums[i])
            i +=1
        else:
            result.append(nums[j])
            j -= 1
        b += 1
    # if n % 2:
    #     result.append(nums[i])
    print(*result)