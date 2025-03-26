class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
    # Flatten the grid into a 1D list
        nums = [num for row in grid for num in row]
    
    # Check if all numbers have the same remainder when divided by x
        remainder = nums[0] % x
        if any(num % x != remainder for num in nums):
            return -1  # Impossible to make all elements equal
    
    # Sort the numbers to find the median
        nums.sort()
        median = nums[len(nums) // 2]
    
    # Calculate the total operations to make all numbers equal to the median
        operations = sum(abs(num - median) // x for num in nums)
    
        return operations
        