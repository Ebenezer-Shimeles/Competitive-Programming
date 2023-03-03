n = int(input())
boys = list(map(int, input().split()))


m = int(input())
girls = list(map(int, input().split()))

girls.sort()
boys.sort()


i = 0
j = 0
pairs = 0

while i < n:
    
    while j < m:
        if i < n and abs(boys[i] - girls[j]) <= 1:
           # print(boys[i], girls[j])
            pairs += 1
            i += 1
           
        elif i <n and  boys[i] < girls[j]:
            break
        j+=1

    i+=1

print(pairs)

    



