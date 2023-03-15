n, k = map(int, input().split())

dis = list(map(int, input().split()))
af = list(map(int, input().split()))

diff = [0] * n
for i, p in enumerate(dis):
    diff[i] = af[i] - p



bout_diff = [0] * k
bought = [0] * k

for i, 