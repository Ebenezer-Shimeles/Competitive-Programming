t = int(input())

for i in range(t):
    input()
    curr = []
    counts = []

    for j in range(8):
        curr.append(input())
        c = 0
        for k in range(8):
          #  print(f'{len(curr[-1])}')
            if curr[-1][k] == '#':
               c+=1
        counts.append(c)  
        c = 0
    for i in range(len(counts)):
        if counts[i] == 1 and i != 0 and i != len(counts) -1 and counts[i-1] == 2  and counts[i+1] == 2:
           # print(f'{i+1} ')
           m = 0
           while curr[i][m] != '#':
             m += 1
           print(f'{i+1} {m+1}')
               
#print(curr)