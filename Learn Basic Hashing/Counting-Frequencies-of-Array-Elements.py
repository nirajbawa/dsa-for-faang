class Solution:
    
    def countFrequencies(self, nums):
        freq = {}
        
        def helper(i):
            # base case
            if i == len(nums):
                return
            
            # count frequency
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
            # recursive call
            helper(i + 1)
        
        helper(0)
        
        # convert dictionary to required format
        return [[key, value] for key, value in freq.items()]
