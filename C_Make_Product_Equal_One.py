import math
n = int(input())

nums = list(map(int, input().split()))

c = 0
z = 0

for i in range(n):
    if nums[i] == 0:
        z += 1
        c += 1
        nums[i] = 1
    elif nums[i] > 0:
        c += (nums[i] - 1)
        nums[i] = 1
    elif nums[i] < 0:
        c += (-1 - nums[i])
        nums[i] = -1


prod = math.prod(nums)
if prod < 0:
   
    if z == 0:
       c += 2
  

print(c)