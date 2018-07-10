class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return -1
        else:
            refer = {}
            for i in range(len(s)):
                if(refer.has_key(s[i])):
                    refer[s[i]] += 1
                else:
                    refer[s[i]] = 1
            indexs = []
            flag = 1
            for key in refer.keys():
                if(refer[key] > 1):
                    pass
                else:
                    flag = 0
                    indexs.append(list(s).index(key))
            if(flag):
                return -1
            else:
                return min(indexs)
