class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        arr = [0] * 26

        # ex: s = sanpa t = sapna
        for i in range(len(s)):
            sIndex = ord(s[i]) - 97 # stores s in ascii
            tIndex = ord(t[i]) - 97 # stores s in ascii
            arr[sIndex] += 1 
            arr[tIndex] -= 1
        
        for num in arr:
            if num == 0:
                continue
            else:
                return False
        
        return True