class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_len = min(len(string) for string in strs)
        res = ""
        for i in range(shortest_len):
            for j in range(len(strs)):
                char = strs[0][i]
                if char != strs[j][i]:
                    return res
            res += char    
        return res



        