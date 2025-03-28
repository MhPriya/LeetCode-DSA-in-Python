class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = range(100)
        for p in x:
            if n == 2**p:
                return True
        return False

        