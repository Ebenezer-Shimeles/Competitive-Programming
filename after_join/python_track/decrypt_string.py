class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = dict()
        for i in range(1, 27):
            # Generating mappings
            char = 'a'
            char_num = ord(char)
            char_num += i -1
            mapping[str(i)] = str(chr(char_num))
       # print(f'Mappings => {mapping}')

        stack = list()
        for char in s:
            if char == '#':
                num_one = str(stack.pop());
                num_two = str(stack.pop());
                #print(f'F-Index {num_two + num_two}')
                stack.append(mapping[  num_two + num_one])
            else:
                stack.append(int(char))
        #print(f'Before Re: {stack}')
        for i in range(len(stack)):
            if isinstance(stack[i], int):
                stack[i] = mapping[str(stack[i])]
        
        return "".join(stack)
