n, m, k = list(map(int, input().split()))


a = list(map(int, input().split()))



def apply(arr, l, r, d):

    arr[l-1] += d

    if r < n:
        arr[r] -= d


opr = [] 
for _ in range(m):
    opr.append(list(map(int, input().split())))

opr_sum = []

for i in range(m):
    now = [0] * n if i == 0 else opr_sum[i-1].copy()
    l, r, d = opr[i]
    apply(now, l, r, d)



    opr_sum.append(now)




effect = [0] *n


for _ in range(k):
    x, y = list(map(int, input().split()))
    # l, r, d = opr[x-1]
    # apply(l, r,d)
    # l, r, d = opr[y-1]
    # apply(l, r,d)
  
    for j in range(n):
        effect[j] += opr_sum[y-1][j]
        if x !=1:
            effect[j] -= opr_sum[x- 2][j]
    



for i in range(n-1):
    effect[i+1] += effect[i]

for i in range(n):
    a[i] += effect[i]
print(*a)