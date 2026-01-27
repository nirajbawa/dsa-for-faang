class Solution:
    def swap(self, nums, temp, j):
        if j<0:
            return j+1
        if nums[j]<temp:
            return j+1
        nums[j+1] = nums[j]
        return self.swap(nums, temp, j-1)
        
         
        
    def outter(self, nums, n):
        if n == -1:
            return
        self.outter(nums, n-1)
        key = nums[n]
        j = self.swap(nums, key, n-1)
        nums[j] = key
        
    
    def insertionSort(self, nums):
        self.outter(nums, len(nums)-2)
        return nums

s = Solution()
print(s.insertionSort([7, 4, 1, 5, 3]))
