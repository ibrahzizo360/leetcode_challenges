class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        for num in range(2,2*150):
            if num % n == 0 and num % 2 == 0:
                return num
        

        