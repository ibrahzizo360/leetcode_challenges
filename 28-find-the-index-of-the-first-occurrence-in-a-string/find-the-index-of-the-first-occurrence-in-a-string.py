class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        n=len(haystack)
        for r in range(len(needle)-1, n):
            if haystack[l:r+1] == needle:
                return l
            l+=1
        return -1

        