n = int(input())

nums = list(map(int, input().split()))

amazing = 0
if len(nums)  <= 1:
    print(amazing)
else:
    ma = nums[0]
    mi = nums[0]

    for num in nums:
        if num > ma:
           # print(f'new Max ={ma} ')
            amazing +=1
            ma = num
        if num < mi:
           # print(f'new Min ={mi} ')
            amazing +=1
            mi = num
    print(amazing)
