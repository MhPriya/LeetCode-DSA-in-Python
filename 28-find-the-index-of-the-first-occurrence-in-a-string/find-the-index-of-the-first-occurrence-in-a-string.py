class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
    
        for i in range(n - m + 1):  # Iterate only till `n-m` to avoid index out of range
            if haystack[i:i + m] == needle:
                return i  # Return the first occurrence
    
        return -1  # If not found
        