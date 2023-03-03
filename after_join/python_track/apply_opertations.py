class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
        print(f'P = {nums}')


        z_count = 0
        n  = []
        for num in nums:
            if num != 0:
                n.append(num)
            else: z_count += 1
        

        for j in range(z_count):
            n.append(0)
        
        return n