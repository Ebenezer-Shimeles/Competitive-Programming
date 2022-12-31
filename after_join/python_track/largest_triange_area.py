import math

class Solution:
    def can_be_triangle(self, n1, n2, n3):
        return n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2

    def largestPerimeter(self, nums: List[int]) -> int:
        # BIG OWWWWW
        nums_sorted = nums.sort(reverse=True)


        big = float('-inf')
        for i in range(len(nums)):
            for j in range(i):
                for k in range(j):
                    if self.can_be_triangle(nums[i], nums[j], nums[k]):
                         #big = max(big, nums[i] + nums[j]+ nums[k])
                         return nums[i]+nums[j]+nums[k]
        
        return big if not math.isinf(big) else 0