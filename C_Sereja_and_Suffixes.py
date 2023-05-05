n, m = map(int, input().split())

a = list(map(int, input().split()))
l = []
print(a)

for _ in range(m):
    l.append(int(input()))
pref = [0] * n
s = set()
j = n - 1

while j>=0:
    s.add(a[j])
    pref[j] = len(s)
    j -= 1
for o in l:
    print(pref[o-1])