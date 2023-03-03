from collections import defaultdict

n = int(input())

nums = list(map(int, input().split()))

i = 0
j = n - 1
s = defaultdict(int)
s2 = defaultdict(str)
mode = True
non_dist = []
while i < n:
    if nums[i] in s:
        mode = False
        non_dist.append(i)
    
    if not mode and nums[i] not in s:
        s2[nums[i]] = 'I'
    s[nums[i]] += 1
    i += 1

#print(non_dist)
if len(non_dist):
    if s2[nums[non_dist[-1]]]:
        print(non_dist[-1] - non_dist[0])
    else:
         print(non_dist[-1] - non_dist[0]+1)
else:
    print(0)