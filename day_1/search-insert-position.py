class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)

        l, r = 0, N - 1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
          
            elif mid == N - 1 and target > nums[N - 1]:
                return mid + 1
            elif target < nums[mid]:
                r=  mid  -1
            elif target > nums[mid]:
                if target < nums[mid + 1]:
                    return mid + 1
                l = mid  + 1
        return mid
        