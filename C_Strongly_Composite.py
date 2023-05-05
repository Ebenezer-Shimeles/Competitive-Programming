from collections import defaultdict


T = int(input())

for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    primes = defaultdict(int)
    for num in a:

        i = 2
        while i**2 <= num:
            while num % i == 0:
                primes[i] += 1
                num //= i
            i += 1
        if num > 1:
            primes[num] += 1
    answer = 0
    M = 0
    for prime, count in primes.items():
        if count > 1:
            answer += count//2
            M += count % 2
        else:
            M += count
    answer += M//3
    print(answer)
