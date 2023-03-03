class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        i = 0
        n = len(arr)
        found_greater = False
        m = 0
        if n < 3:
            return False
        while i < n:
            if i == 1 and arr[i] < arr[i-1]:
                return False
            if i < n - 1 and i > 0 and arr[i+1] == arr[i]:
                return False
            if i < n - 1 and arr[i] > arr[i+1] and arr[i] > arr[i-1] and  i > 0 :
                found_greater = True
                m = arr[i]
                break
            i += 1
        if not found_greater:
            return found_greater
        is_decreasing = True
        print(f'Checking decrease m = {m}')
        while i< n:
            if i < n - 1 and arr[i] <= arr[i+1]:
                is_decreasing = False
                break
            i +=1
        return is_decreasing