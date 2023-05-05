t = int(input())

for _ in range(t):
    N = int(input())
    a = list(map(int, input().split()))
    l, r = 0, N -1
    #print(l, a)
    found = True
    chosen = None

    def is_pali(dele, start, end):
        while start < end:
            if a[start] != a[end]:
                if a[start] == dele:
                    start += 1
                elif a[end] == dele:
                    end -= 1
                else:
                    return False
            else:
                start += 1
                end -= 1
        return True

    while l < r:
        if a[l] == a[r]:
            l += 1
            r -= 1
        elif chosen:
            if a[l] == chosen:
                l += 1
            elif a[r] == chosen:
                r -= 1
            else:
                found = False
                break
        else:
            found = is_pali(a[l], l, r) or is_pali(a[r], l, r)
            break

    if found:
        print('YES')
    else:
        print("NO")