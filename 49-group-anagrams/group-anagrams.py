class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        res = []
        for word in strs:
            key = tuple(sorted(word))
            hashMap[key].append(word)
        for v in hashMap.values():
            res.append(v)
        return res