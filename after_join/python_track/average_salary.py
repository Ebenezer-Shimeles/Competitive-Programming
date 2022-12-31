class Solution:
    def average(self, salary: List[int]) -> float:
        l = len(salary)
        small = salary[0]
        big = salary[0]
        s = 0

        for sal in salary:
            s += sal
            small = min(small, sal)
            big  = max(big, sal)
        
        return (s - small - big )/(l - 2)