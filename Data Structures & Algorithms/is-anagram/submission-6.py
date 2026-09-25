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

        for i in range(n):
            hashed_s[s[i]] = 1 + hashed_s.get(s[i], 0)
            hashed_t[t[i]] = 1 + hashed_t.get(t[i], 0)

        if hashed_s == hashed_t:
            return True
        else:
            return False