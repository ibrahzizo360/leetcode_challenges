class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiples = [ n * i for i in range(1, 150)]
        evenMultiples = []
        for num in multiples:
            if num % 2 == 0:
                evenMultiples.append(num)

        return evenMultiples[0]

        