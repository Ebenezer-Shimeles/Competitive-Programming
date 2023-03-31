import bisect
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a.sort()

res = []
d = dict()
for i, num in enumerate(a):
    d[num] = i

for num in b:
    res.append(bisect.bisect_right(a, num))  
    




print(*res)