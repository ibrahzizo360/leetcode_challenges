class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numsMap = Counter(nums)
        bucket = [[] for i in range(len(nums) +1)]
        for num, count in numsMap.items():
            if len(bucket[count]) == 0:
                bucket[count] = [num]
            else:    
                bucket[count].append(num)    
        for arr in bucket[::-1]:
            if len(arr) !=0:
                for i in arr:
                    res.append(i)
            if len(res) == k:
                return res


        