class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        nums = nums[::-1]
        print(nums)
        return nums[k-1]
        