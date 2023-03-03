

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    i = 0
    j = n-1

    while j > i:

        if (s[j] == '1' and s[i] == '0') or (s[j] == '0' and s[i] == '1'):
            j -= 1
            i += 1
        else:
            print(j-i+1)
            break
    if j == i:
        print(1)
    elif j < i:
        print(0)