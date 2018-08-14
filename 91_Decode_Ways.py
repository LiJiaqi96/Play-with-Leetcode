class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s[0]=='0'): 
            return 0
        K=[1]*len(s)
        for i in range(1, len(s)):
            if(s[i-1] + s[i] == '00'): 
                return 0
            elif(s[i-1] == '0' and (1 <= int(s[i]) <= 9)):
                K[i] = K[i-1]
            elif(s[i-1] in ['1','2'] and s[i] == '0' and i > 1):
                K[i] = K[i-2]
            elif(s[i-1] in ['1','2'] and s[i] == '0'):
                K[i] = K[i-1]
            elif(3 <= int(s[i-1]) <= 9 and s[i] == '0'):
                return 0
            elif(s[i-1] + s[i] >= '27'):
                K[i] = K[i-1]
            else:
                K[i] = K[i-1] + K[i-2]
        
        return K[-1]
