class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 0
        seq_map = defaultdict(int)
        res = []

        for r in range(9, len(s)):
            seq = s[l:r+1]
            if seq in seq_map:
                seq_map[seq] += 1
            else:
                seq_map[seq] += 1
            l+=1

        for k, v in seq_map.items():
            if v > 1:
                res.append(k)

        return res


        