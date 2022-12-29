class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        print(f'as string {s}')

        for i in range(len(s)//2):
            if s[i] != s[len(s) - 1 - i]:
                return False;
        return True