class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        counter = Counter(s)
        res = counter[letter] / len(s) * 100
        print(res)
        return int(res)