n = int(input())

words = []
for i in range(n):
    words.append(input())

def is_long(w: str):
    if len(w) > 10:
        return True
    else: 
        return False
def tr(w: str):
   # print(f'tr {w}')
    return_value = w[0] 
    c = 0
    for i in range(1, len(w) - 1):
       c+=1
    return_value += str(i)
    return_value += w[-1]
    return return_value

for word in words:
    if is_long(word):
        print(tr(word))
    else:
        print(word)