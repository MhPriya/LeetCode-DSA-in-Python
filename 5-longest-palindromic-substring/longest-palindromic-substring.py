class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        longest = ""
    
        for i in range(n):  # Start index
            for j in range(i, n):  # End index
                substring = s[i:j+1]  # Extract substring
                if substring == substring[::-1]:  # Check if it's a palindrome
                    if len(substring) > len(longest):
                        longest = substring  # Update longest palindrome
    
        return longest