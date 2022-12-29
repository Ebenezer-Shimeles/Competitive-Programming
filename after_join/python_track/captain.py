K = int(input())
entries = list(map(int,  input().split(' ')))

m = dict()

for i in range(len(entries)):
    # O(n)
    key = str(entries[i])
    if  key in m:
        m[key] += 1
    else:
        m[key] = 1

for key, n in m.items():
    if n == 1:
        print(key)
        break
