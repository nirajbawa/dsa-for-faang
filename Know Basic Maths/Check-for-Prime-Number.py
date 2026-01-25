class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        for i in range(2, round(n/2)):
            if n%i == 0:
                return False
        return True