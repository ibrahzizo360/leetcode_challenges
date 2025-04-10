class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = defaultdict(int)
        return len(nums) != len(set(nums))
        