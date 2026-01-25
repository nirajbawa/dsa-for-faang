class Solution:
    def GCD(self, n1, n2):
        i = min(n1, n2)
        while(i>0):
            if n1%i==0 and n2%i==0:
                return i
            i  = i-1

        return 1