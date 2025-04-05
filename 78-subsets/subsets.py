class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, current):
            if index == len(nums):
                res.append(current[:])  # Add a copy of the current subset
                return
            # Include nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()
            # Exclude nums[index]
            backtrack(index + 1, current)

        backtrack(0, [])
        return res