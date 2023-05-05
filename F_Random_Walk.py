t = int(input())
import math

for _ in range(t):
    N = int(input())
    a = list(map(int, input().split()))
    p_a = math.prod(a)
    print(p_a)