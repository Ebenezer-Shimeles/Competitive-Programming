class Solution:
    def count_pairs(self, n):
        return_value = 0

        for i in range(n):
            return_value += i
        return return_value

    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = dict()
        return_value = 0
        for num in nums:
            key = str(num)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1
        for key, count in map.items():
            print(f'Count:{key} {count}')
            return_value += self.count_pairs(count)
        return return_value