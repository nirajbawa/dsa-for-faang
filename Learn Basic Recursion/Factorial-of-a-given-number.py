class Solution:
    def factorial(self, n):
        if n==1:
            return 1;
        if n==0:
            return 1;
        
        return self.factorial(n-1)*n
        