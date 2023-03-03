n = int(input())

def is_distinct(n: int):
    n = str(n)
    
    return len(n) == len(set(n))

i = n + 1

while not is_distinct(i):
    i += 1
print(i)
