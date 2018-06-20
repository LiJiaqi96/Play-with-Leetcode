class Solution(object):
    def trailingZeroes(self,n):
        """
        :type n: int
        :rtype: int
        """
        nums = 0
        i = 1
        while(n // 5**i > 0):
            nums = n//5**i + nums
            i += 1
        return nums		
