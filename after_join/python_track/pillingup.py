# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())




def is_possible(n: int, lens):
    stack = list()
    i = 1
    
    for i in range(n-1):
        next_elem = None;
    #     if i %2: #right
    #         next_elem = lens.pop()
    #     else:  #left
    #         next_elem = lens.pop(0)
    #     i += 1
    #     if not len(stack):
    #         stack.append(next_elem)
    #         continue 
    #     elif next_elem > stack[-1]:
    #        # print(f'Not Successful {stack}')
    #         return False
    #     stack.append(next_elem)
    # #print(f'Successful {stack}')
        first = lens[0]
        last = lens[len(lens) - 1]
        
        if first >= last:
            next_elem = first
            lens.pop(0)
        elif last > first:
            next_elem = last
            lens.pop()
        
        if len(lens) == 1:
            return True
        
        first = lens[0]
        last = lens[len(lens) - 1]
        
        if first > next_elem or last > next_elem:
            return False
    return True

for i in range(T):
    n = int(input())
    lens = list(map(int, input().split()))
    if is_possible(n, lens):
        print('Yes')
    else:
        print('No')