n, t = map(int, input().split())

q = list(input())


for _ in range(t):
    i = 0
    while i < n:
        if q[i] == 'B' and i < n - 1 and  q[i+1] == 'G':
            q[i], q[i+1] = q[i+1], q[i]
            i += 1
        i += 1
print("".join(q))