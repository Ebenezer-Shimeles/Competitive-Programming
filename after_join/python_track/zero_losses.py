class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # loop throught each element and set winning and lossing 
        # loop through the map and get 1 and zeros
        m = dict()
        
        for match in matches:
            key_one = str(match[0])
            key_two = str(match[1])

            if key_one in  m:
                m[key_one][0] += 1
            else:
                m[key_one] = [1, 0]
            
            if key_two in  m:
                m[key_two][1] += 1
            else:
                m[key_two] = [0, 1]
        not_lost = []
        one_lost = []
        for  player,values in m.items():
            print(f'{player}: {values}')
            if values[1] == 1:
                one_lost.append(int(player))
            elif values[1] == 0:
                not_lost.append(int(player))
        not_lost.sort()
        one_lost.sort()
        return [not_lost, one_lost]