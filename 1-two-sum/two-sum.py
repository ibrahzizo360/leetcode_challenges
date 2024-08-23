class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hashmap.values():
                for k,v in hashmap.items():
                    if v == res:
                        return [i, k]
            hashmap[i] = nums[i]