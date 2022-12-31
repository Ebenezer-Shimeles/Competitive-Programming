class Solution:
    def interpret(self, command: str) -> str:
        return_value = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                return_value += 'G'
                print(f'Ret Val: {return_value}')
                i +=1
            elif command[i] == '(':
                if command[i+1] == ')':
                    return_value += 'o'
                    print(f'Ret Val: {return_value}')
                    i += 2
                elif command[i+1:i+3] == 'al':
                    
                    return_value += 'al'
                    print(f'Ret Val: {return_value}')
                    i += 3
            else: i += 1
        return return_value