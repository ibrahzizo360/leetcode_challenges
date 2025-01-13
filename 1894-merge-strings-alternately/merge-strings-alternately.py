class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n = max(len(word1), len(word2));
        i,j = 0,0
        for char in range(n):
            if char < len(word1):
                res += word1[char]
            if char < len(word2):
                res += word2[char]

        return res
       