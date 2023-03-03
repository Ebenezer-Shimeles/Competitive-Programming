class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        arr = [ ]
        for i in range(1, n+1):
            arr.append(i)
        i = 0
        while len(arr) > 1:
            i = (k+i - 1) % len(arr)
            arr.pop(i)
         
           
        return arr[0]
