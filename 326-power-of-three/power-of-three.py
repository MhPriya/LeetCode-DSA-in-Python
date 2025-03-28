class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        x = range(100)
        for xp in x:
            if n == 3 ** xp:
                return True
        return False
        