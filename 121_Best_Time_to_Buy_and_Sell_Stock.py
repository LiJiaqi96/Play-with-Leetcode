class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(prices == []):
            return 0 
        else:
            result = 0
            buy = max(prices) + 1
            for i in range(len(prices)):
                if(prices[i] < buy):
                    buy = prices[i]
                elif(prices[i] - buy > result):
                    result = prices[i] - buy
                else:
                    pass
            return result

