class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Step 1: Sort the array
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
        # Skip duplicate values to optimize
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

            # If an exact match is found, return immediately
                if current_sum == target:
                    return current_sum
            
            # Update closest_sum if this sum is closer
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
            
            # Move pointers intelligently
                if current_sum < target:
                    left += 1
                # Skip duplicate values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                # Skip duplicate values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return closest_sum

                        
        