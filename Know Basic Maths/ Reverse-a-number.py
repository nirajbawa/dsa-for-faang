class Solution:
    def __init__(self):
        self.revNum = 0
    def reverseNumber(self, n):
        while n>0:
            lastDigit = n%10
            self.revNum = self.revNum*10 + lastDigit
            n = n//10
        return self.revNum