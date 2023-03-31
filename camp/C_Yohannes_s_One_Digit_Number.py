
num = input()

def trans(num: str) -> str:
    n = 0
    for ch in num:
        n += int(ch)
    return str(n)

if len(num) == 1:
    print('0')
else:
    tries = 0

    while True:
        num = trans(num)
        tries += 1
        if len(num) == 1:
            break
    print(tries)