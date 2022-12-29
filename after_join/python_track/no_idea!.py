# Enter your code here. Read input from STDIN. Print output to STDOUT
happyness = 0
N, M  = input().split(' ')

N = int(N)
M = int(M)

ints = list()
ints_string = input().split(' ')



for i in range(len(ints_string)):
    ints.append(int(ints_string[i]))

#print(f'Ints = {ints}')

set_a = set()
set_b = set()

set_a_raw = input().split(' ')
set_b_raw = input().split(' ')

for i in range(M):
    set_a.add(int(set_a_raw[i]))
    set_b.add(int(set_b_raw[i]))

#print(f'Set A = {set_a}, Set B = {set_b}')
for i in range(N):
    if ints[i] in set_a:
        happyness +=1
    elif ints[i] in set_b:
        happyness -= 1

print(happyness)




