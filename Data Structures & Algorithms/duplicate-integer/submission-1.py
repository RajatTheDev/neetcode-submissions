class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        for key, value in my_dict.items():
            if value > 1:
                return True
        
        return False