n = int(input())
coins = list(map(int, input().split()))


took = []
while sum(took) <= sum(coins):
    m = max(coins)
    coins.remove(m)
    took.append(m)
print(len(took)) 