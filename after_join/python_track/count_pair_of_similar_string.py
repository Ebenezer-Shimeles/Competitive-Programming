class Solution:
    def pair_count(self, k: int):
        return_value = 0
        print(k)
        for i in range(k):
            return_value += i
        return return_value

    def similarPairs(self, words: List[str]) -> int:
        map = dict()
        

        pairs = 0
        for word in words:
            l = list(set(word))
            l.sort()
            key = "".join(l)

            if key in map:
                map[key] += 1
            else:
                map[key] = 1
        
        for key, count in map.items():
            t= self.pair_count(count)
            print(f't = {t}')
            pairs += t
        return pairs