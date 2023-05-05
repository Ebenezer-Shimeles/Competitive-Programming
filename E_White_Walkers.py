num, l, r = map(int, input().split())

def f(x):
    if x == 0 or x == 1:
        return 1
    else:
        return 2 * f(x//2) + 1

T = f(num)

res = 0
def g(x, start = 1):
    global res
    if start > r or start < l:
        print(x, start)
        return
    # if r not in range(start, v+1) and l not in range(start, v+1):
    #     print('no',x,  start, v)
    #     return
    
    if x %2:
        res += 1
    if x == 1 or x == 0:
        return
    else:
        g(x//2, start )
        g(x//2, start + 2)
    
g(num)
print(res)