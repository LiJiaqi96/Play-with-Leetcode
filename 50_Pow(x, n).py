class Solution(object):
    def __init__(self):
        self.refer = {}
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n in self.refer.keys()):
            return self.refer[n]
        else:
            if(n == 0):
                self.refer[n] = 1.0
                return 1.0
            elif(n == 1):
                self.refer[n] = x
                return x
            elif(n < 0):
                n = 0 - n
                x = 1.0/x
            else:
                pass
            if(n % 2 == 0):
                self.refer[n] = self.myPow(x,n/2) * self.myPow(x,n/2)
                return self.myPow(x,n/2) * self.myPow(x,n/2)
            else:
                self.refer[n] = self.myPow(x,n/2) * self.myPow(x,n/2) * x
                return self.myPow(x,n/2) * self.myPow(x,n/2) * x
