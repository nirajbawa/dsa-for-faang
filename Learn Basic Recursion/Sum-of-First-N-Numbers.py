class Solution:
    def NnumbersSum(self, N):
        if N==0:
            return 0;
        return self.NnumbersSum(N-1)+N