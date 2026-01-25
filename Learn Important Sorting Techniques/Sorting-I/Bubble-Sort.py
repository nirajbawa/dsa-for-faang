class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            flag = 0
            for j in range(n-1-i):
                if(nums[j]>nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = 1
            if(flag==0):
                break
        return nums

s = Solution()
print(s.bubbleSort( [7, 4, 1, 5, 3]))