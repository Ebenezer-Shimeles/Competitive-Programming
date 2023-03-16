class Solution:
    def invert(sefl, s:str) -> str:
        rv = []

        for ch in s:
            if ch == '0':
                rv.append('1')
            else:
                rv.append('0')
        return "".join(rv)
    def make_str(self, n) ->str:
        if n == 1:
            return "0"
        else:
            before =  self.make_str(n-1)
            return before+ "1" + (self.invert(before))[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        
        made = self.make_str(n)
        print(made)
        return made[k-1]