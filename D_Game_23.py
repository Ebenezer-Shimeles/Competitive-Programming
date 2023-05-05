n, m = map(int, input().split())

ways = -1
def check(curr, t,times):
    global ways
    if curr > m:
        return
    if curr == m:
        if t:
            ways =  t - 1
        else:
            ways = 0
        return
    else:
        check(curr * times, t + 1, 2)
        check(curr * times, t + 1, 3)
check(n ,0, 1)
print(ways)