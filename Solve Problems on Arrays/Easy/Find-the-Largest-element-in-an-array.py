class Solution:
    def largestElement(self, nums):
        min = -2**31
        for i in range(len(nums)):
            if nums[i] > min:
                min = nums[i]
        return min