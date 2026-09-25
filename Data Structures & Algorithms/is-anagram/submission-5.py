class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        
        # Handling edge cases
        if len(t) != n:
            return False
        elif len(t) == 0 or n == 0:
            return False
        
        # Sorting method
        hashed_s = {}
        hashed_t = {}

        for ch in s:
            if ch in hashed_s:
                hashed_s[ch] += 1
            else:
                hashed_s[ch] = 1
        
        for ch in t:
            if ch in hashed_t:
                hashed_t[ch] += 1
            else:
                hashed_t[ch] = 1

        if hashed_s == hashed_t:
            return True
        else:
            return False