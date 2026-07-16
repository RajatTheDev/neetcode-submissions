class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1 # decrease since we swapped the value
            else:
                left += 1 # increase if the left is safe
        return left 