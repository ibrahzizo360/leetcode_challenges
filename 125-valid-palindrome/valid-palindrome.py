class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = re.sub("[^A-Za-z0-9]","",s).lower().replace(" ","")
        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] == chars[j]:
                i+=1
                j-=1
            else: return False
        return True
        