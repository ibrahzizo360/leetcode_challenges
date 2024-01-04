class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        print(t)
        print(s)
        if s == t:
            return True