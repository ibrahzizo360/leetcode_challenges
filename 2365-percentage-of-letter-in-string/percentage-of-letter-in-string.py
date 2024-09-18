class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        counter = Counter(s)
        for k,v in counter.items():
            if k == letter:
                return int((v/len(s)) * 100)
        return 0

        