n = int(input())

a = list(map(int, input().split()))

a.sort()
sum_left = 0
sum_right = 0

# for i in range(n):
#     sum_left += a[i]
# for i in range(n, 2*n):
#     sum_right += a[i]

# if sum_right != sum_left:
#     print(*a)


k = 0
j = 2*n - 1

is_found = False
while k < j:
    sum_left, sum_right = 0, 0 
    for i in range(n):
        sum_left += a[i]
    for i in range(n, 2*n):
        sum_right += a[i]
    if sum_right != sum_left:
        print(*a)
        is_found = True
        break

    a[k], a[j] = a[j], a[k]
    k += 1
    j -= 1
if not is_found:
    print(-1)

