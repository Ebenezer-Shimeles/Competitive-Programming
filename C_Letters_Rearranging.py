
def getAllCombination(s: str):
    if(len(s) == 1):
        return [s]
    return_value = []
    n = len(s)
    s_l = list(s)
    for i in range(n):
       combs = s[n-1-i:]
       for j in range(len(combs)):
          return_value.append("".join(s[:n-1-i]) + "".join(getAllCombination("".join(combs))))

    return return_value
def is_pali(s:str):

    i = 0
    n =  len(s)
    while i < n//2:
      if s[i] != s[n - 1 - i]:
        return False
      i+=1
    return True

t = int(input())
#print(is_pali("abba"))
for i in range(t):
    word = input()
    if len(set(word)) == 1:
        print("-1")
    else:
        r = [word[0]]
        first_letter = word[0]
        k = 0
        for i in range(1, len(word)):
            if word[0] != word[i]:
                r.append(word[i])
                k = i
                break
        for i in range(1, len(word)):
            if i!=k:
               r.insert(1, word[i])
        print("".join(r))
                