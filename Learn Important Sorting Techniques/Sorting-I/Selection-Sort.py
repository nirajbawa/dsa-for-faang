class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                if(nums[j]<nums[min]):
                    min = j
            if(min!=j):
                nums[i] = nums[min]
        return nums

s = Solution()
print(s.selectionSort( [7, 4, 1, 5, 3]))