class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum = 0
        prefix = list()

        for i in reversed(range(0, len(nums) - 1)):
            prefix.insert(i, sum )
            sum += nums[i]
        
        sum  = 0
        for i in range(0, len(nums) - 1):
            if sum == prefix[i]: return i 
            sum += nums[i]
        print(prefix)
        return -1