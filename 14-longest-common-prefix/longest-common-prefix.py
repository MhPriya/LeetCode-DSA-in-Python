class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):  # Iterate through characters of the first string
            char = strs[0][i]  # Take the character at index i
            for s in strs[1:]:  # Compare with other strings
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]  # Return the prefix found so far
        return strs[0]  # If no mismatch, return the full first string
        