class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lengths = []
        for index in wordDict:
            lengths.append(len(index))
        lengths = sorted(list(set(lengths)))
        dp = [True] + [False]*len(s)
        for i in range(len(dp)-1):
            if(dp[i]):
                for j in lengths:
                    if(i+j >= len(dp)):
                        break
                    elif(s[i:i+j] in wordDict):
                        dp[i+j] = True
        print(dp)
        return dp[-1]
        
                    
       
