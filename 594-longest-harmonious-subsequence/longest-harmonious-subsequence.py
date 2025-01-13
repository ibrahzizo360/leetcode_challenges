class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_len = 0
        for k,v in counter.items():
            if k+1 in counter:
                max_len = max(max_len, v + counter[k + 1]) 
        return max_len
        