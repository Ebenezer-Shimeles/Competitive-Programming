class Solution:
    def insert(self, nums: List[int], n, sz):
        print(f'Checking for {n}')
        for i, num in enumerate(nums):
            if num >= n:
                print(f'{num} > {n} inserting at {i-1}')
                nums.insert(i, n)
                #nums.pop()
                break
            if num == 0 and i>=sz :
                nums.insert(i, n)
                break

    #[-1,0,0,3,3,3,0,0,0]
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = n
        for i, n in enumerate(nums2):
            self.insert(nums1, n, i+m)
        for i in range(t):
            c = nums1.pop()
            print(f'Poped {c}')

        # i1 = 0
        # i2 = 0

        # while i1 < m and i2 < n:
        #     if nums1[i1] >= nums2[i2]:
        #         nums1.insert(i1, nums2[i2])
        #         i2 += 1
        #         i1 += 1
        #         nums1.pop()

        #     else:
        #         i1 += 1
        # if i2 < n:
        #     for i in range(n-i2):
        #         nums1.pop()
        #     nums1.extend(nums2[i2:])
        