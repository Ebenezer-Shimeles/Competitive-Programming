class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        smallest = min(nums)
        biggest = max(nums)

        # O(2N)
        map = dict()
        for num in nums:
            map[str(num)] = 1
        # 
        for i in range(0, len(nums)):
            if not str(i) in map:
                return i
        return biggest+1