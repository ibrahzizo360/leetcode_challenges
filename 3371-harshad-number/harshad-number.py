class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits = list(str(x))

        digit_sum = sum(int(num) for num in digits)
        if x % digit_sum == 0:
            return digit_sum
        return -1
        