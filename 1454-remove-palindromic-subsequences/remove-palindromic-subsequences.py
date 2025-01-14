class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Check if the string is a palindrome
        if s == s[::-1]:
            return 1
        # If not a palindrome, it will always take 2 steps
        return 2