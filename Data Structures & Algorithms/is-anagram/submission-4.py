class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        
        # Handling edge cases
        if len(t) != n:
            return False
        elif len(t) == 0 or n == 0:
            return False
        
        # Sorting method
        s = sorted(s)
        t = sorted(t)
        for i in range(n):
            if s[i] != t[i]:
                return False
        return True