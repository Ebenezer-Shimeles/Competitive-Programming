class Solution:

    def int_to_str(self, i: int):
        return_value = ""
        tmp = i
        
        if i == 0:
            return "0"
        while tmp:
            return_value += str(tmp % 10)
            tmp //=10
        return self.reverse(return_value)

    def multiply(self, num1: str, num2: str) -> str:
        num1_val = 0;
        num2_val = 0
        
        # p is power
        num1_reversed = self.reverse(num1)
        num2_reversed = self.reverse(num2)

        print(f'RNum1 = {num1_reversed} RNum2 = {num2_reversed}')

        for p, num_char in enumerate(num1_reversed):
            num1_val += (10 ** p) * (ord(num_char) - ord('0'))
     
        for p, num_char in enumerate(num2_reversed):
            num2_val += (10 ** p) * (ord(num_char) - ord('0'))

        prod = num1_val * num2_val

        print(f'Prod = {prod}')
        return self.int_to_str(prod)
    
    def reverse(self, s: str):
        return s[::-1]