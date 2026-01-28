class Solution:
    
    def partion(self, nums, lb, ub):
        pivot = nums[lb]
        
        start = lb
        end = ub
        
        while(start<=end):
            while(start <= ub and nums[start]<=pivot):
                start +=1
            
            while(nums[end]>pivot):
                end -=1
            
            if(start<end):
                nums[start], nums[end] = nums[end], nums[start]
            
        nums[lb], nums[end] = nums[end], nums[lb]
        return end
                
    
    def quickSortMain(self, nums, lb, ub):
        if lb < ub:
            loc = self.partion(nums, lb, ub)
            self.quickSortMain(nums, lb, loc-1)
            self.quickSortMain(nums, loc+1, ub)
        
    def quickSort(self, nums):
        self.quickSortMain(nums, 0, len(nums)-1)
        return nums

s = Solution()
print(s.quickSort([5, 4, 4, 1, 1]))