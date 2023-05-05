import math
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    
    nums = 0
    evens = 0
    for i, num in enumerate(a):
        nums += 1
        k = i + 1
        while k % 2 == 0:
            k //=2
            evens += 1
        while num % 2 ==0:
            num //=2
            evens += 1
    print(nums, evens)
