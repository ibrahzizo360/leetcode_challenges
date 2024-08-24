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
            print("sorted", sortedString)
            if sortedString in hashmap:
                # if string not in hashmap[sortedString]:
                hashmap[sortedString].append(string) 
            else:
                hashmap[sortedString] = [string]

        res = []
        for k,v in hashmap.items():
            res.append(v)
        print(res)
        print(hashmap)
        return res

        