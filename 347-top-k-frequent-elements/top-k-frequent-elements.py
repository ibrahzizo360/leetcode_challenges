class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countMap = Counter(nums)
        res = [item for item, count in countMap.most_common(k)]
        return res

        