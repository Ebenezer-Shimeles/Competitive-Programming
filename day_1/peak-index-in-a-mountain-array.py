class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        l, r = 0, N- 1

        while l <=r:
            mid = (l+r)//2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

        return l