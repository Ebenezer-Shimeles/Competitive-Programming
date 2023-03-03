s, n = list(map(int, input().split()))

bonuses = [] # This stores the strength and bonus comibnation
strengths = []

for i in range(n):
    x, y = list(map(int, input().split()))
    bonuses.append(y)
    strengths.append(x)

is_safe = True
while len(strengths):
    less = []
    for i in range(len(strengths)):
        if s > strengths[i]:
            less.append(i)
    
    if(not len(less)):
        print('NO')
        is_safe = False
        break
    max_bonus_id = 0 # in the less
    for i in range(len(less)):
        # now we find the max bonus
        if bonuses[less[i]] > bonuses[less[max_bonus_id]]:
            max_bonus_id = i
   
    s += bonuses[less[max_bonus_id]]
    bonuses.pop(less[max_bonus_id])
    strengths.pop(less[max_bonus_id])
if is_safe:
   print('YES')
