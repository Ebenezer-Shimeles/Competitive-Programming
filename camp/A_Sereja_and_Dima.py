n = int(input())

nums = list(map(int, input().split()))

i = 0
j = n - 1

serja = 0
dima = 0

b = True

while i < j:
    if b:
       #sereja
        if nums[i] > nums[j]:
           serja += nums[i]
           i += 1
        else:
            serja += nums[j]
            j-=1
    else:
        if nums[i] > nums[j]:
            dima += nums[i]
            i += 1
        else:
            dima += nums[j]
            j -= 1
    b = not b
if i == j:
    if not b:
        dima += nums[i]
    else:
        serja += nums[i]
print(serja, dima)