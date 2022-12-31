class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return_value = ""
        small = min(map(len, [word1, word2]))
        

        for i in range(2*(small)):

             if ((i + 1) % 2):
                 print(f'#1 {i}')
                 return_value += word1[(i + 1)//2]
             else:
                  print(f'#2 {i}')
                  return_value += word2[(i)//2]
        len_1 = len(word1)
        len_2 =  len(word2)
        
        if len_1 > len_2:
            return_value += word1[small:]
        elif len_2 > len_1:
            return_value += word2[small:]
        

        return return_value