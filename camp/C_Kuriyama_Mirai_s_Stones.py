n = int(input())
v = list(map(int, input().split()))
m = int(input())

prefs = [0] * n

sorted_prefs = sorted(v)

for i in range(n):
    prefs[i] = v[i]

for i in range(n-1):
    prefs[i+1] += prefs[i]

for i in range(n-1):
    sorted_prefs[i+1] += sorted_prefs[i]

for _ in range(m):
    type, l, r = list(map(int, input().split()))
    if type == 1:
        if l == 1:
            print(prefs[r-1])
        else:
            print(prefs[r-1] - prefs[l-2])
    else:
        if l == 1:
            print(sorted_prefs[r-1])
        else:
            print(sorted_prefs[r-1] - sorted_prefs[l-2])
