class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            I could use couting sort but I try to use insertion sort here.
            we assum the first index(0) is already sorted
            then we insert a new element in the correct place with every iteration
        """
        n = len(nums)

        if n == 1:
            return
        
        unsorted_index = 1
        while unsorted_index < n: 
            tmp = nums[unsorted_index]
            c_index = unsorted_index
            # Here insertion happens
            while c_index > 0 and tmp < nums[c_index-1]:
                nums[c_index] = nums[c_index-1]
                c_index -= 1
            nums[c_index] = tmp
            unsorted_index += 1


        

        