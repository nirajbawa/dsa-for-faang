class Solution:
    def swap(self, nums, i, n):
        if i ==  n - 1:
            return
    
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
        self.swap(nums, i+1, n)

    def outloop(self, nums, n):
        if n == 1:
            return
        print(n)
        self.swap(nums, 0, n)
        self.outloop(nums, n-1)

    def bubbleSort(self, nums):
        self.outloop(nums, len(nums))
        return nums