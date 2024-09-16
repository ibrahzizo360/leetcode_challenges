class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_str = min(strs, key=len)
        for i in range(len(min(strs, key=len))):
            for string in strs:
                if shortest_str[i] != string[i]:
                    return shortest_str[:i]
        return shortest_str
        