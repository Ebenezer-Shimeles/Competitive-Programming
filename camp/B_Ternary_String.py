from collections import defaultdict

t = int(input())

for _ in range(t):
    s = input()
    m = defaultdict(int)
    N = len(s)
    left, right = 0, 0
    
    min_len = float('inf')

    while right < N:
        m[s[right]] += 1
        
        
        while len(m) == 3:

            min_len = min(min_len, right-left +1)
            m[s[left]] -= 1
            if m[s[left]]  == 0:
                del m[s[left]] 
            left += 1
            

       
        right += 1
    if min_len == float('inf'):
        print(0)
    else:
        print(min_len)