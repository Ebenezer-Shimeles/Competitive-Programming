import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)

        return pow(4, n//2, mod=mod) * pow(5, math.ceil(n /2), mod=mod) % mod
        