class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common = [*words[0]]

        for i in range(1, len(words)):
            # now check every spelling
            word = [*words[i]]
            c_copy = common.copy()
            print(f'common = {common}')
            for i  in range(len(common)):
                ch = common[i]
                print(f'checking {ch} in {word}')

                if ch not in word:
                    # while ch in common:
                    c_copy.remove(ch)
                  #  print(f'{ch} not found in {word} {words[i]} common = {common}')
                    
                    
                else:
                    print('removing ')
                    word.remove(ch)
            common = c_copy
        return common