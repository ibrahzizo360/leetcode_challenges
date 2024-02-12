class Solution:
    def maxArea(self, height: List[int]) -> int:
        waterArea = 0
        i = 0
        j = len(height) - 1

        while i < j:
            if height[i] < height[j]:
                length = j - i
                width = min(height[i], height[j])
                curArea = length * width
                waterArea = max(curArea, waterArea)
                i+=1
            elif height[i] >= height[j]:
                length = j - i
                width = min(height[i], height[j])
                curArea = length * width
                waterArea = max(curArea, waterArea)
                j-=1

        return waterArea        

            