class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #brute force with TC:O(n**4) SC:O(1)
        # n = len(nums)
        # res = set()
        # nums.sort()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range (j+1, n):
        #             for l in range(k+1, n):
        #                 if nums[i]+ nums[j] +nums[k] +nums[l] == target:
        #                     res.add((nums[i],nums[j], nums[k], nums[l]))

        # return list(res)

        nums.sort()
        n = len(nums)
        res =[]

        if not nums or len(nums) < 4:
            return []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, n):
                if j > i+1 and nums[j]== nums[j-1]:
                    continue
                left , right = j+1 ,  n-1

                while left < right :
                    total = nums[i]+ nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        right -= 1
                        while left < right  and nums[left]== nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right +1 ]:
                            right -= 1
                        
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
    

