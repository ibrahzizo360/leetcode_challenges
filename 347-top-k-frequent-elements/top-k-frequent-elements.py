class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = Counter(nums)
        res = []
        print('numsMap: ', numsMap)
        curVals = list(numsMap.values())
        print("curVals: ", curVals)
        c = 0
        while c < k:
            curMax = max(curVals)
            print("curMax: ", curMax)
            for key,val in numsMap.items():
                if val == curMax:
                    print('key: ', key)
                    res.append(key)
                    numsMap.pop(key)
                    break
            curVals.remove(curMax)
            c+=1
        return res
        
