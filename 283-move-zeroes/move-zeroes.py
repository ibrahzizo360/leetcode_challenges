class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero = 0
        zero_count = 0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1
            else:
                zero_count += 1

        for i in range(non_zero, n):
            nums[i] = 0
              


        