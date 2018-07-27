class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)
        refer1 = {}
        refer2 = {}
        flag1 = 1
        flag2 = 1
        for i in range(len(s_list)):
            if(refer1.has_key(s_list[i])):
                if(refer1[s_list[i]] == t_list[i]):
                    pass
                else:
                    flag1 = 0
                    break
            else:
                refer1[s_list[i]] = t_list[i]

        for j in range(len(t_list)):
            if(refer2.has_key(t_list[j])):
                if(refer2[t_list[j]] == s_list[j]):
                    pass
                else:
                    flag2 = 0
                    break
            else:
                refer2[t_list[j]] = s_list[j]
        flag = flag1 and flag2
        if(flag):
            return True
        else:
            return False
