pages = list(set(map(int, input().split(','))))
pages.sort()

n = len(pages)

l = []

i = 0
j = 0

pgs = []
while i < n:

    start = i
    j = i
    while j < n - 1:
        if pages[j] == pages[j+ 1] -1:
            j += 1
        else: break
    if j - i:
        pgs.append([pages[i], pages[j]])
    else:
        pgs.append(pages[i])
    i = j + 1
return_value = []
for pg in pgs:
    if isinstance(pg, int):
        return_value.append(f"{pg}")
    else:
        return_value.append(f'{pg[0]}-{pg[1]}')
print(",".join(return_value))
        
