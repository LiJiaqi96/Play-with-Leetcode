class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_dict = {}
        result = []
        for i in range(len(s)-9):
            s_temp = s[i:i+10]
            if(s_dict.has_key(s_temp)):
                s_dict[s_temp] += 1
            else:
                s_dict[s_temp] = 1
        for key in s_dict.keys():
            if(s_dict[key] > 1):
                result.append(key)
            else:
                pass
        return result
