class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n <= 2):
            return 0
        else:
            primes = [1] * n
            primes[0] = 0
            primes[1] = 0
            for i in range(2,n):
                if(primes[i]):
                    for j in range(2,(n-1)//i+1):
                        primes[i*j] = 0
                else:
                    pass
            return sum(primes)
        
