class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) < 1):
            return ""
        elif(len(strs) == 1):
            return strs[0]
        else:
            min_length = min([len(strs[m]) for m in range(len(strs))])
            result = []
            i = 0
            flag = 0
            while(i < min_length):
                temp = strs[0][i]
                for j in range(1,len(strs)):
                    if(strs[j][i] == temp):
                        flag = 1
                    else:
                        flag = 0
                        break
                if(flag):
                    result.append(temp)
                else:
                    break
                i += 1
            return ''.join(result)
