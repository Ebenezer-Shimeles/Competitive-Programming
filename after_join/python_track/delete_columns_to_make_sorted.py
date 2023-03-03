class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        d = 0
        n = len(strs[0])

        for i in range(n):
            prev = strs[0][i]
            for s in strs:
               if s[i] < prev:
                   print(f'wrong at {s[i]} {prev}')
                   d += 1
                   break
               prev = s[i]

        return d