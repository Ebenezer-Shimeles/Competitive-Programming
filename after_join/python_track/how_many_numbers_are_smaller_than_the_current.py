class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
           O(n)

           Approach:
              1) Find the max number
              2) Make an array of lengh m, each element initialized to 0
              3) Increment every index so that it becomes frequency counting
              4) Make the array culumlative to know the index and that is how much 
        '''

        m  = max(nums)
        cumm = [0 for i in range(m+1)]
        return_value = []
       
        for num in nums:
           print(num)
           cumm[num] += 1 # Frequency counting
        print(cumm)
        for i in range(m):
            cumm[i+1] += cumm[i] # Making it cumulative
        print(cumm)
        for i in range(len(nums)):
            if nums[i] == 0:
                return_value.append(0)
            else:
                return_value.append(cumm[nums[i] - 1])
        return return_value
        