class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:  # Found an element to keep
                nums[k] = nums[i]  # Move it to the front
                k += 1  # Increment valid count

        return k 
        