n,m,k = list(map(int, input().split()))

grid = [input() for i in range(n)]




def get(n, k):
    h=  1 + n - k
    if h >=0:
        return h
    return 0

c = 0
t = 0

for i in range(n):
    t = 0
    o = grid[i].split('*')
    for s in o:
        c += get(len(s),k)

for i in range(m):
    for j in range(n):
       
        if grid[j][i] == '*':
            c += get(t, k)
            t = 0
        elif grid[j][i] == '.':
            t += 1
    if t:
        c += get(t, k)
    t = 0
if n == 1 and m == 1:
    if c:
        print(1)
    else:
        print(0)
else:
    print(c)