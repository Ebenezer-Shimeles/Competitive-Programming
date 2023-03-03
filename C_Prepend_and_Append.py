t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    i = 0
    j = n - 1

    while i < j:

        if (s[i] == '0' and s[j] == '1') or (s[i] == '1' and s[j] == '0'):
            i += 1
            j -= 1
        else:
            break
    print(j-i + 1)