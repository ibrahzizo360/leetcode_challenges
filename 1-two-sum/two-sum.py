class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in hash:
                return [hash[diff],i]
            hash[v] = i    

           