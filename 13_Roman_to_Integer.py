class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        sums = 0
        s_dict = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0
        while(i < len(s_list)-1):
            if(s_dict[s_list[i]] >= s_dict[s_list[i+1]]):
                sums += s_dict[s_list[i]]
                i += 1
            else:
                sums += (s_dict[s_list[i+1]]-s_dict[s_list[i]])
                i +=2
        if(i == len(s_list)-1):
            sums += s_dict[s_list[i]]
        else:
            pass
        return sums
