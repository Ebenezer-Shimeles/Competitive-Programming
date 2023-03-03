t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    l = 0
    r = 0
    count = 0 
    '''[1 0 0 0 0 11  10]'''
                 
    while l < n:
        #r = l - 1
        while r < n-1 and nums[l] == nums[r+1]:
            r += 1
        # if r == n:
        #     r -= 1
        
        if (l == 0 or nums[l-1] > nums[l]) and (r == n - 1  or nums[r+1] > nums[r]):
            count += 1
        l = r + 1


    
  
    if count == 1:
        print('YES')
    else:
        print('NO')