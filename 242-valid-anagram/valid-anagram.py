from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force method TC:O(nlogn) & SC:O(n)
        # if len(s)!= len(t):
        #     return False
        # return sorted(s) == sorted(t)
        # if len(s)!=len(t):
        #     return False
        # count_s, count_t= Counter(s), Counter(t)
        # return count_s == count_t
        if len(s) != len(t):
            return False
        c_s, c_t = Counter(s),Counter(t)
        return c_s == c_t

