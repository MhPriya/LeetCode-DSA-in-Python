class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Store last seen index of characters
        left = 0
        m_length = 0
    
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # Move left pointer
        
            char_index[s[right]] = right  # Update last seen index
            m_length = max(m_length, right - left + 1)  # Update max length
    
        return m_length
        