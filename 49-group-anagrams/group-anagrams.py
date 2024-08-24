class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            hashmap[sorted_string].append(string)
        
        return list(hashmap.values())

        