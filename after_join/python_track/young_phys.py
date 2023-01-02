n = int(input())


result = [0, 0, 0]
for i in range(n):
     x, y, z = list(map(int,  input().split()))
     result[0] += x
     result[1] += y
     result[2] += z

if result[0] == 0 and result[1] == 0 and result[2] == 0:
    print('YES')
else:
    print('NO')