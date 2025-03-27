class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # Convert list of digits to an integer
        # num = int("".join(map(str, digits)))  
        # # Add 1
        # num += 1  
        # # Convert back to list of digits
        # return list(map(int, str(num)))
        num = int("".join(map(str, digits)))
        num+=1
        return list (map(int  ,str(num)))
        