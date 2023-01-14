class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        gt = []
        lt = []
        eq = []

        for n in nums:
           if n > pivot: gt.append(n)
           elif n  == pivot: eq.append(n)
           elif n < pivot: lt.append(n)
        return lt + eq +gt