class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0 or n == 1):
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in xrange(2, n+1):
            dp[i] = 2*dp[i-1]
            for j in xrange(1, i-1):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[i]
