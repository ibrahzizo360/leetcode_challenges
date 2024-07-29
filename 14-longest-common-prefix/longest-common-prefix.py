class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        shortest_str = min(strs, key=len)

        for i in range(len(shortest_str)):
            char = shortest_str[i]
            for string in strs:
                if char != string[i]:
                    return shortest_str[:i]
        return shortest_str

        