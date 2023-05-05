q = int(input())
from collections import Counter

res = []
def combinations(sides):
    s= set()
    def dfs(i, curr):
      

        
        if len(curr) == 4:
            c = Counter(curr)
            for num in curr:
                if c[num] < 2:
                    return
            res.append(sorted(curr.copy()))

           
            return
        if i >= len(sides):
            return
        curr.append(sides[i])
        dfs(i+1, curr.copy())
        curr.pop()
        dfs(i+1, curr.copy())

    dfs(0, [])
    
for _ in range(q):
    n = int(input())
    sides = list(map(int, input().split()))
    side_set = Counter(sides)
    
    for side in sides:
        if side_set[side] == 1:
            print('NO')
            break
    combinations(sides)
    areas = []
    for L, _, W, __ in res:
        areas.append(L * W)
    c = Counter(areas)
    found = False
    print(res)
    for a in areas:
        if c[a] == n:
            print("YES")
            found = True
            break
    if not found:
        print("NO")
     
    res.clear()
   