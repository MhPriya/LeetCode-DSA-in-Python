class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):  # Traverse from right to left
            curr_value = roman_map[char]
            if curr_value < prev_value:  # If smaller than the previous, subtract it
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value  # Update previous value
            
        return total
        