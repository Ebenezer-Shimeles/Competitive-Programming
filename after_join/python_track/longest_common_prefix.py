class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        if len(strs) == 1:
            return strs[0]
        return_value = ""
        current_index = 0
        m_len = min(map(len, strs))
        


        for i in range(m_len): # Which character ?
            current_char = strs[0][i];
            for j in range(len(strs)): # Which word?
                 if strs[j][i] != current_char:
                     return return_value;
            return_value += current_char
        return return_value # just in case
            