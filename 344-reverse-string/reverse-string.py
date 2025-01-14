class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1  # Initialize two pointers

        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the pointers closer
            left += 1
            right -= 1
        
        