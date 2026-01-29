class Solution:
    def secondLargestElement(self, nums):
        large_ele = [-2**31] * 2

        def push(ele):
            
            ele1 = large_ele.pop()
            ele2 = large_ele.pop()

            newele1 = max(ele1, ele2)
            
            if newele1 > ele:
                large_ele.append(newele1)
                large_ele.append(ele)
            elif newele1==ele:
                large_ele.append(ele2)
                large_ele.append(ele1)
            else:
                large_ele.append(ele)
                large_ele.append(newele1)

        for i in range(len(nums)):
            top = large_ele[-1] if large_ele else None
            if nums[i] > top:
                push(nums[i])
                
            
        return -1 if min(large_ele) == -2**31 else min(large_ele)

s = Solution()
print(s.secondLargestElement( [10, 10, 10, 10, 10]))