class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1  # Start checking from 1
        while x * x <= num:
            if x * x == num:
                return True
            x += 1
        return False