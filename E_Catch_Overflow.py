from collections import deque
l = int(input())

stack = deque()
times_stack = []
x = 0
last_times = deque()
for _ in range(l):
    cmd = input()
    
    if cmd.startswith('for'):
        stack.append('(')
        times = int(cmd.split(' ')[1])
        #times_stack.append(times)
        last_times.appendleft(times)
    elif cmd == 'end':
         stack.append(')')
         times_stack.extend(last_times)
         last_times.clear()
    elif cmd == 'add':
        stack.append('+')
#print(*stack)
#print(times_stack)

def interpret(stack, times = 1):
    #print(f'got ', *stack, f'times = {times}')
    global x
    
    c = 0
    new_stack = deque()
    mode =False
    while stack:
        s = stack.pop()
        if s == '+' and not mode:
           x += times
        if s == ')':
            mode = True
            c -= 1
        elif s == '(':
            c += 1
        if mode and c:
            new_stack.appendleft(s)
        
        if (s == '(') and c == 0 and mode:
            new_stack.pop()
            interpret( new_stack, times * times_stack.pop())
            c = 0
            mode = False
        #print(x)

    


interpret(stack)
if x <= (2**32) - 1:
    print(x)
else:
    print("OVERFLOW!!!")



