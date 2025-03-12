class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force method
        # n = len(nums)
        # triplets =[]
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] +nums[j] +nums[k] == 0:
        #                 triplets.append((nums[i],nums[j],nums[k]))
        # return triplets

        #optimised one
        nums.sort()
        n = len(nums)
        triplets = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets