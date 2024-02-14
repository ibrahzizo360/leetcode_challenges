class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        max_l = height[l]
        max_r = height[r]
        water = 0

        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

            if max_l < max_r:
                calc = min(max_l, max_r) - height[l]
                water += calc if calc > 0 else 0
                l+=1

            else:
                calc = min(max_l, max_r) - height[r]
                water += calc if calc > 0 else 0
                r-=1

        return water    