class Solution:
    
    def is_correct(self, word_one: str, word_two: str, pre_map: dict):
          m_len = min(map(len, [word_one, word_two]))      
          for i in range(m_len):
              if pre_map[word_one[i]] > pre_map[word_two[i]]:
                  print(f'{pre_map[word_one[i]]}({word_one[i]}) > {pre_map[word_two[i]]}({word_two[i]})')
                  return False
              elif  pre_map[word_one[i]] < pre_map[word_two[i]]:
                   return True
              elif  pre_map[word_one[i]] ==  pre_map[word_two[i]]:
                   continue
          if len(word_one) > len(word_two):
              return False
          return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pre_map = dict()
        for i in range(len(order)):
            pre_map[order[i]] = i


        if len(words) == 1:
            return True
        
        for i in range(len(words) - 1):
              if not self.is_correct(words[i], words[i+1], pre_map):
                  return False
        return True