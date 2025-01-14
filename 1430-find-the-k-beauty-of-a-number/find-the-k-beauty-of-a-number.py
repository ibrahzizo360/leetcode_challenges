class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        num_str = str(num)

        for i in range(len(num_str) - k +1):
            sub_str = num_str[i:k+i]

            if int(sub_str) != 0 and num % int(sub_str) == 0:
                count+=1
        
        return count
        