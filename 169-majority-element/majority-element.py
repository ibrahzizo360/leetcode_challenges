class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashNum = Counter(nums)
        return [key for key,val in hashNum.items() if max(hashNum.values()) == val][0]

        