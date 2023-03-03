n, m = list(map(int, input().split()))

nums_one = list(map(int, input().split()))
nums_two = list(map(int, input().split()))

cumm = [0] * m

i = 0 # tracks nums_two
j = 0 # tracks nums_one

while i < m:
    lt = 0 # The number of less than the current number
    
    while j < n and nums_one[j] < nums_two[i]:
        j += 1
        lt += 1
    cumm[i] = cumm[i-1] + lt


    i += 1

print(*cumm)