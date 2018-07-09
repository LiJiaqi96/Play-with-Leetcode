class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        temp = []
        flag = 0
        if(s == ''):
            return ''
        else:
            for i in range(len(s)):
                if(s[i] != ' '):
                    temp.append(s[i])
                else:
                    if(i < len(s)-1 and s[i+1] == ' '):
                        pass
                    else:
                        flag =1
                        result.append(''.join(temp))
                        temp = []
            result.append(''.join(temp))
            if(result[0] == ''):
                del result[0]
            if(result[-1] == ''):
                del result[-1]
            new_result = [result[x] for x in range(len(result)-1,-1,-1)]
            return ' '.join(new_result)
