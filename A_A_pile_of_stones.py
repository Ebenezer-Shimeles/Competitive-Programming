n = int(input())
s = input()

n = 0

for ch in s:
    if ch == '-':
        if n > 0:
            n -=1
    else:
        n += 1
print(n)
