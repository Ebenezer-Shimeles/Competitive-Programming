class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights)

        l, r = max(weights), sum(weights)
        mi = float('inf')
        while l<= r:
            mid = (l + r)//2
            c_sum = 0
            d = 0
            i = 0
            #print(('--'*6) + f'mid: {mid}')
            while i < N:
                c_sum += weights[i]
                if c_sum == mid:
                    d += 1
                    #print(f'c_sum {c_sum} i: {i} day: {d}')
                    c_sum = 0
                elif c_sum > mid:
                    
                    d += 1
                    #print(f'c_sum {c_sum} day: {d}')

                    c_sum = 0
                    i -= 1
                i += 1
            if c_sum:
                d += 1
            if d > days:
                l = mid +1
            elif d <= days:
                mi = min(mi, mid)
                r = mid - 1 
                
          
        return mi