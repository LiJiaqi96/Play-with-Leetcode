class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        if(s == []):
            return []
        else:
            indexs = []
            for i in range(len(s)):
                if(s[i] in vowels):
                    indexs.append(i)
                else:
                    pass
            s_list = list(s)
            for j in range(len(indexs)/2):
                m,n = indexs[j],indexs[~j]
                s_list[m],s_list[n] = s_list[n],s_list[m]
            return ''.join(s_list)
                    
