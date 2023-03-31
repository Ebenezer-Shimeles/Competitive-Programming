# n, left, r = list(map(int, input().split()))

# def is_ones_z(n):
#     for num in n:
#         if num != 1 and num != 0:
#             return False
#     return True


# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)
# else:
#     l = [n]
    
#     while not is_ones_z(l):
#         n = len(l)
#         i = 0
#         while i < n:
#             if l[i] > 1:
#              x = l.pop(i)
#              l.insert(i, x//2)
#              l.insert(i + 1, x % 2)
#              l.insert(i+1, x//2)
         
#              i += 3
#             else:
#                 i += 1
#     i = left - 1
#     count = 0
#     while i < r:
#         if l[i] == 1:
#             count += 1
#         i += 1
#     print(count)
n, left, r = list(map(int, input().split()))
def unlock(n):
    rv = []
    if n == 0 or n == 1:
        return [n]
    if n % 2:
        j = unlock(n//2)
        rv.extend(j)
        rv.append(1)
        rv.extend(j)
    else:
        j = unlock(n//2)
        rv.extend(j)
        rv.append(0)
        rv.extend(j)
    return rv
u = unlock(n)
left -= 1
count = 0
while left < r:
    
    if u[left] == 1:
        count += 1
    left += 1
print(count)