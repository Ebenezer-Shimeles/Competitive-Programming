t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()

    if  c == 'g':
        print(0)
    else:
        c_s = []
        g_s = []

        for i in range(n):
            if s[i] == c:
                c_s.append(i)
            elif s[i] == 'g':
                g_s.append(i)

        m = float('inf')

        
        i = -1
       
        ans = float('-inf')
        for i in range(len(c_s)):
            d = float('inf')
            for j in range(len(g_s)):
                # d = min(d, c_s[i] - g_s[j])
                if c_s[i] > g_s[j]:
                    m = n - c_s[i] + g_s[j]
                elif c_s[i] < g_s[j] :
                    m = g_s[j] - c_s[i]
                d = min(m,  d)
              
            ans = max(ans, d)
        
            
        # for j in range(len(g_s)):

        #         if c_s[i] > g_s[j]:
        #             m = max(m, n - c_s[i] + g_s[j])
        #         elif c_s[i] < g_s[j] :
        #             m = (m, g_s[j] - c_s[i])
              

                


        print(ans)
     
    
