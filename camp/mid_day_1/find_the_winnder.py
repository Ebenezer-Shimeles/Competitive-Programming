class Solution:
    def rec(self,nums: List[int], l, r, mode: bool  = True):
       
        if l > r:
            return 0
        if mode:
            return max(nums[l]+self.rec(nums, l+1, r, False),
                     nums[r]+self.rec(nums, l, r-1, False)
            
            )
        else:
            return min(self.rec(nums, l+1, r, True), self.rec(nums,
                l, r-1, True))
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        s = sum(nums)
        N = len(nums)
        m = self.rec(nums, 0, N-1)
       
        if s - m <= m:
            return True
        return False
        