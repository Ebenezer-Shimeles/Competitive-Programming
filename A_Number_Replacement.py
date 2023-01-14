t = int(input())


for i in range(t):
    n = int(input())
    nums = input().split()#list(map(int, input().split()))
    chars = input()
    m = dict()
    
    error = False
    for j in range(n):
        
        if nums[j] in m:
            if chars[j] != m[nums[j]]:
                error = True
                print('NO')
                break
        else:
            m[nums[j]] = chars[j]
    if not error:
        print('YES')
   