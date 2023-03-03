n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

if len(nums) >= k:
    gt = nums[k-1]


    count = 0 
    for i in range(len(nums)):
        if nums[i] >= gt and nums[i] != 0:
            count += 1

    print(count)
else:
    print(len(nums))