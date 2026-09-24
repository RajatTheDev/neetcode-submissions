class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # Handling edge case
        if n == 0:
            return False

        # Sorting method
        nums.sort()
        c_no = nums[0]
        for i in range(1, n):
            if c_no == nums[i]:
                return True
            else:
                c_no = nums[i]
        return False