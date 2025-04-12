class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        legit_count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[legit_count] = nums[i]
            legit_count += 1

        return legit_count