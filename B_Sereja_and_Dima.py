n = int(input())
nums = list(map(int, input().split()))

s = 0
dima = 0
mode = True # s's
i = 0
j = n - 1

while i < j:
    
    first = nums[i]
    last = nums[j]

    if first > last:
        if mode:
            s += nums[i]
           
        else:
            dima += nums[i]
         
        i += 1
    elif last > first:
        if mode:
            s+= last
          
        else:
            dima += last
          
        j -= 1
    mode = not mode
if n % 2:
    s += nums[i]
else: 
    dima += nums[j]
print(s, dima)
