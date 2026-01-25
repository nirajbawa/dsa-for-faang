class Solution:
    def isArmstrong(self, n):
        n = abs(n)
        n_c = n
        n_c_t = n
        val = 0
        nfd = 0
        while n>0:
            ld = n%10
            nfd = nfd+1
            n = n//10
        
        while n_c > 0:
            ld = n_c % 10
            val = (ld ** nfd) + val
            n_c = n_c // 10

        return val == n_c_t