class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0  # Pointer to place the next non-zero element

        # Step 1: Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # Step 2: Fill the remaining elements with 0
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0