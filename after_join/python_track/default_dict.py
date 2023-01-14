# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

d = defaultdict(list)

n, m = list(map(int, input().split()))
B = []

for i in range(n):
    d[input()].append(i)
for i in range(m):
    B.append(input())

for i in range(m):
    if B[i] in d:
        print(" ".join(map(str, map(lambda x: x + 1 , d[B[i]]))))
    else:
        print('-1')
