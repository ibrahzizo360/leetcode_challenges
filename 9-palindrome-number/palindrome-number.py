class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        new = str(x)[::-1]
        if str(new) == str(x):
            return True
        

        