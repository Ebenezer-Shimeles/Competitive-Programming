
N = int(input())
s = []
for  _ in range(N):
    s.append(int(input()))
s.sort()


l, r = (N-1)//2, N-1

m = N
while l >=0 and m >N//2:
    if 2 * s[l] <= (s[r]):
        m -= 1
        r -= 1
    l -= 1



print(m)