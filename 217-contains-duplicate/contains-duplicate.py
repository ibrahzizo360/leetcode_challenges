class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = defaultdict(int)
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] += 1 
        return False
        