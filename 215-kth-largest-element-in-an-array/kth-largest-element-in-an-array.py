class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
        # return nums[k-1]
        min_heap = []

        for num in nums:
            heapq = heappush(min_heap , num)
            if len(min_heap) > k:
                heapq = heappop(min_heap)
        return min_heap[0]
        