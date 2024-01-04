class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            sortedword = ''.join(sorted(word))
            anagramMap[sortedword].append(word)   

        return anagramMap.values()    
        