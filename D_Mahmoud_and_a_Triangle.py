n = int(input())

lines = list(map(int, input().split()))

lines.sort()
lines.reverse()
found = False
for i in range(len(lines) - 2):
    if lines[i] < lines[i+1] + lines[i+2] and  lines[i+1] < lines[i] + lines[i+2] and  lines[i+2] < lines[i+1] + lines[i+1]:
        found = True
        break


if found:
    print('YES')
else:
    print('NO')