class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        max_l = 0
        max_r = 0
        water = 0

        if not height: return 0

        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            print("max_l", max_l)
            print("max_r", max_r)

            if max_l < max_r:
                calc = min(max_l, max_r) - height[l]
                result = calc if calc > 0 else 0
                water += result
                l+=1

            else:
                calc = min(max_l, max_r) - height[r]
                result = calc if calc > 0 else 0
                water += result
                r-=1

        return water    