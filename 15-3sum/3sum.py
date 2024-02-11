class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):

            if i > 0 and nums[i-1] == nums[i]:
                    continue

            l, r = i+1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum > 0:
                    r-=1

                if curSum < 0:
                    l+=1
                
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r:
                        l+=1
                       
        return res



        