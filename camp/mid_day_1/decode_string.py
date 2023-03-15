class Solution:
    def decodeString(self, s: str) -> str:
    
        N = len(s)
        ptr = 0
        
        current_num = ""
        current_string = ""

        stack = deque()
        while ptr < N:
            #print(ptr, s, N)
            c = s[ptr]
            if c.isnumeric():
                current_num += c
            
            elif c == '[':
              
                stack.append(current_string)
                stack.append(int(current_num))
                current_string = ""
                current_num = ""
            elif c == ']':
                n = stack.pop()
                
                st = stack.pop()

                current_string = st + current_string * n
            else:
                 current_string += c
                 
            ptr += 1
        return current_string

            


        