from collections import Counter
N = int(input())
s = list(map(int, input().split()))

s.sort()
#print(s)


c = Counter(s)
j = N - 1
m = 0
while j >= 0:
    if c[s[j]] <= 0:
        j -= 1
        continue
    elif s[j] == 3:
        if c[1] >= 1:
           c[1] -=1
           
    elif s[j] == 2:
        if c[1] >= 2:
            c[1] -= 2
        elif c[2] >= 2:
            c[2] -= 1
        elif c[1] ==1:  #GREEDY
            c[1] -= 1
    elif s[j] == 1:
        if c[1] >= 4:
            c[1] -= 3
        else:
            c[1] -= (c[1] - 1)
    c[s[j]] -= 1
    m += 1
    j -= 1

print(m)