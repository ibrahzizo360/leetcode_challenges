class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            char_set = set(sub)
            for char in char_set:
                if char.lower() not in char_set or char.upper() not in char_set:
                    return False
            return True
        
        max_len = 0
        res = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_nice(s[i:j+1]):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        res = s[i:j+1]
        
        return res