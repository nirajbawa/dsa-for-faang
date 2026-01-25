class Solution:    
    def palindromeCheck(self, s):
        def helper(l, r):
            if l>=r:
                return True
            elif s[l]!=s[r]:
                return False
            return helper(l+1, r-1)
        return helper(0, len(s)-1)