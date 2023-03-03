from typing import List

n  = int(input())
nums = list(map(int, input().split()))



def is_odd(n: int):
    return n % 2

odds = 0
evens = 0

for num in nums:
    if is_odd(num):
        odds += 1
    else:
        evens += 1
    if evens and odds:
        nums.sort()

print(*nums)