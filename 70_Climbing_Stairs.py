class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(num):
            factorial = 1
            if(num < 0):
                return "error"
            elif num == 0:
                return 1
            else:
                for i in range(1,num + 1):
                    factorial = factorial*i
                return factorial

        def cases(total,sel):
            return (factorial(total)/(factorial(sel)*factorial(total-sel)))

        two = n / 2
        remain = n % 2
        ways = 0
        if(two == 0):
            ways = remain
        else:
            for i in range(two+1):
                total = i + 2*(two-i) + remain
                sel = i
                ways += cases(total,sel)
        return ways
