s = input()

n = len(s)

if n < 26:
    print(-1)
else:
    found = False
    accepted = 0
    
    i = 0
    start = i
    ins = set()
    correct = []
    alphabet = [ chr(i) for i in range(ord('A'), ord('Z')+1) ]
    alpha_set = set(alphabet)

    end = 0
    while i < n:
        
        if s[i] in ins and s[i] != '?':
            ins.clear()
            correct.clear()
            accepted = 0
            start = i
            continue
        else:
            correct.append(s[i])
            ins.add(s[i])
            accepted += 1
            i += 1
        if accepted == 26:
            end = i
            found = True
            for  ch in correct:
               if ch in alpha_set:
                alpha_set.remove(ch)
            
            for i, ch in enumerate(correct):
                if ch == '?':
                    v = alpha_set.pop()
                    correct[i] = v
            break
                   
    
    if found:
        print("".join(correct) )


    if not found:
        print(-1)