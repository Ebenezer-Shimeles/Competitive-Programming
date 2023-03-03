n, m = list(map(int, input().split()))

nums_one = list(map(int, input().split()))
nums_two = list(map(int, input().split()))

merged = []

i = 0
j = 0

while i < n and j < m:
    if nums_one[i] < nums_two[j]:
        merged.append(nums_one[i])
        i += 1
    else:
        merged.append(nums_two[j])
        j +=1
if ( i < n):
    merged.extend(nums_one[i:])
if  (j < m):
    merged.extend(nums_two[j:])


print(*merged)