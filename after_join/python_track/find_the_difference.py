class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_arr = [*t]
        s_arr = [*s]
        
        for i in range(len(s_arr)):
            t_arr.remove(s_arr[i]);
        return t_arr[0]