n = int(input())

a = list(map(int, input().split()))
b = sorted(a)

l, r = 0, 0
i = 1
while i < n:
    if a[i - 1] > a[i]: #descreasing
        l = i - 1
        while  i < n and a[i - 1] > a[i]:
            i += 1
        r = i - 1
        break
    i += 1
ans = []
for i in range(l):
    ans.append(a[i])
ans.extend(a[l:r+1][::-1])
for i in range(r+1, n):
    ans.append(a[i])
#print(ans)
if ans == b:
    print('yes')
    print(f'{l+1} {r+1}')
else:
    print('no')