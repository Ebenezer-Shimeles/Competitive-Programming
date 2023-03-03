n = int(input())

nums = list(map(int, input().split()))

nums.sort()


pos = []
neg = []
zero =  []

neg_t = []

for num in nums:
    if num == 0:
        zero.append(0)
    elif num > 0:
        pos.append(num)
    elif num < 0:
        neg_t.append(num)

''' 
so if negativ is even we need to add one in the neg
and the rest in zero
'''

if len(pos) == 0:
    if len(neg_t) % 2:
        # add the last to negative and the rest to posit
        pos.extend(neg_t[:-1])
        neg.append(neg_t[-1])
    else:
        pos.extend(neg_t[:-2])
        neg.append(neg_t[-2])
        zero.append(neg_t[-1])
else:
    neg.append(neg_t[-1])
    zero.extend(neg_t[:-1])

print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)
# print(len(neg), end=' ')
# for i in range(len(neg)):
#     print(neg[i], end= ' ')
# print('')
# print(len(pos), end=' ')
# for i in range(len(pos)):
#     print(pos[i], end= ' ')
# print('')
# print(len(zero), end=' ')
# for i in range(len(zero)):
#     print(zero[i], end= ' ')

