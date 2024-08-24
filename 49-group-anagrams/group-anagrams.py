class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(str)
        for string in strs:
            sortedString = sorted(string)
            sortedString = ''.join(sortedString)
            if sortedString in hashmap:
                hashmap[sortedString].append(string) 
            else:
                hashmap[sortedString] = [string]

        res = []
        for k,v in hashmap.items():
            res.append(v)
        return res

        