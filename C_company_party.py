from collections import defaultdict, deque
n = int(input())

roots = deque()
lows = deque()
k = 1
m = defaultdict(list)
for i in range(n):
    p = int(input())

    if p == -1:
        roots.append(i + 1)
    else:
        m[p].append(i + 1)
while roots or lows:
    
    if not roots:
        if lows:
            k += 1
        roots.extend(lows)
        lows.clear()
    t = roots.popleft()
    
    lows.extend(m[t])
print(k)
# print(m, roots)
