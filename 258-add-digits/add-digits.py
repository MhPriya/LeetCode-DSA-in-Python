class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1+(num-1)% 9
        # There is a mathematical formula to find the digital root: 
        # Digital Root = 1 + ( \U0001d45b \U0001d462 \U0001d45a − 1 ) m o d 9 


        