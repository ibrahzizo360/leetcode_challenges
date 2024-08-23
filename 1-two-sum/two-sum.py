class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = defaultdict(int)
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [idx, hashMap[diff]]
            hashMap[val] = idx   