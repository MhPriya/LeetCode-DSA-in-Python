class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)  # O(m + n) for merging and O((m+n) log (m+n)) for sorting

    # Step 2: Find the median
        n = len(merged)
        if n % 2 == 1:  # Odd length
            return float(merged[n // 2])
        else:  # Even length
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0