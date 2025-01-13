class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        n = len(nums)
        for k,v in counter.items():
            if v > n / 2:
                return k
        return res
        