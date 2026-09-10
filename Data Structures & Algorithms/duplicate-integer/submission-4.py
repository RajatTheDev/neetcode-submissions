class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = -1
        for i in range(len(nums)):
            if prev == nums[i]:
                return True
            else:
                prev = nums[i]
        return False