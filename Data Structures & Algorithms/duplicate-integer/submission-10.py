class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # Handling edge case
        if n <= 1:
            return False

        # Hashset Method
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return True
        
        return False