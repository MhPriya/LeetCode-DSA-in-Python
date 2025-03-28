class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        new_num = range(100)
        for nn in new_num:
            if n == 4 ** nn:
                return True 
        return False
        