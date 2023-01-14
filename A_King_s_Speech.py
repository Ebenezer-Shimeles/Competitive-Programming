n = int(input())

def t(word: str):
    first = word[:2]
    first += '... '
    first += word
    first += '?'
    return first

words = []
for i in range(n):
    word = input()
    words.append(word)
    
for word in words:
    print(t(word))