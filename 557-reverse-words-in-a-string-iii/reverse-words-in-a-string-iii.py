class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = [word[::-1] for word in words]
        res = ''
        for i in range(len(words)):
            res += words[i]
            if i != len(words)-1:
                res += ' '
        return res

        