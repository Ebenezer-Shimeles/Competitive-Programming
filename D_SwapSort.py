from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))

mins = sorted(nums)

locations = defaultdict(list)
swaps = []

for i in range(n):
    locations[nums[i]].append(i)

i = 0
j = 0

while i < n and j < n:

    arr = locations[mins[j]]
    me = locations[nums[i]]

 

  
    nums[arr[-1]], nums[i] = nums[i], nums[arr[-1]]
    new_loc = arr[-1]
    swaps.append([arr[-1], i])
    me.remove(i)
    me.append(new_loc)
    arr.pop()

  
    j += 1
    i += 1

print(len(swaps))
for swp in swaps:
    print(*swp)
