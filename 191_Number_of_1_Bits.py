class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_list = list(bin(n)[2:])
        return binary_list.count('1')
