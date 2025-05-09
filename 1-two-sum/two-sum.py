class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     num_to_index = {}
    
    # # Iterate over the list of numbers
    #     for index, num in enumerate(nums):
    #     # Calculate the complement that would sum up to the target
    #         complement = target - num
        
    #     # Check if the complement exists in the dictionary
    #         if complement in num_to_index:
    #         # If found, return the indices of the complement and the current number
    #             return [num_to_index[complement], index]
        
    #     # Otherwise, add the current number and its index to the dictionary
    #         num_to_index[num] = index
    
    # # If no solution is found, return an empty list
    #     return []

        num_too_index = {}
        for index, n in enumerate(nums):
            complement = target - n
            if complement in num_too_index:
                return(num_too_index[complement], index)
            num_too_index[n]= index
        return[]
