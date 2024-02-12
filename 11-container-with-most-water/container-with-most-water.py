class Solution:
    def maxArea(self, height: List[int]) -> int:
        waterArea = 0
        i = 0
        j = len(height) - 1

        while i < j:
            curArea = (j - i) * min(height[i], height[j])
            if height[i] < height[j]:
                waterArea = max(curArea, waterArea)
                i+=1

            elif height[i] >= height[j]:
                waterArea = max(curArea, waterArea)
                j-=1

        return waterArea        

            