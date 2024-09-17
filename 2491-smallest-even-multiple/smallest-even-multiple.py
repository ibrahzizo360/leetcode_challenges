class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = n*2
        if n % n == 0 and n % 2 == 0:
            return n
        else:
            return product

        