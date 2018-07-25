class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        re_binary = bin(n)[2:].rjust(32, '0')[::-1]
        return int(re_binary,2)
        
