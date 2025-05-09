class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n*(n+1)//2
        new_sum = sum(nums)
        return exp_sum - new_sum
        