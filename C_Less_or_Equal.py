n, k = map(int, input().split())
nums = list(map(int, input().split()))


nums.sort()

o = -1
if k == 0:
    o = nums[0] - 1

elif k == len(nums):

    o = nums[-1]
else:
     
    if nums[k-1] == nums[k]:
        o = -1
    else:
        o = nums[k-1]
if o >= 1 and o <= 10** 9:
    print(o)
else:
    print(-1)
#1000000000

