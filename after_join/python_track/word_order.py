# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

m = dict()
l = list();

for i in range(N):
    word = input()
  
    if word in m:
        m[word] += 1
    else:
        l.append(word)
        m[word] = 1

print(len(m.items()))

for i in range(len(l)):
    print(m[l[i]], end=' ')