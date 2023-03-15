t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    m = float('-inf')
    for i in range(n):
        for j in range(m):
            