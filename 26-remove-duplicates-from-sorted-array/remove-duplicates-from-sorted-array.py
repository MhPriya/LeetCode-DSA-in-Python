class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Edge case: Empty list
            return 0

        k = 1  # Pointer for unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Found a new unique element
                nums[k] = nums[i]  # Place it at the correct position
                k += 1  # Move pointer for unique elements

        return k  # Number of unique elements