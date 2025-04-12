class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        res = []
        for word in strs:
            key = tuple(sorted(word))
            hashMap[key].append(word)
            
            # if sorted(word) in hashMap:
            #     hashMap[sorted(word)].append(word)
            # else:
            #     hashMap[sorted(word)].append(word)
        for v in hashMap.values():
            res.append(v)
        print(res)
        return res