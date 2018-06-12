class Solution:
    def run_temp(self,s, index, repeat_times, s_new):    
        s_temp = []
        i = index
        while i < len(s):
            if s[i].isalpha():
                s_temp.append(s[i])
                i += 1
            elif s[i] == "[":
                i += 1
            elif s[i] == "]":
                for j in range(repeat_times):
                    s_new += s_temp
                return i+1
            else:
                numstr = []
                while(s[i].isdigit()):
                    numstr += s[i]
                    i += 1
                num = ''.join(numstr)
                num = int(num)
                s_1 = []
                i = self.run_temp(s, i, num, s_1)
                s_temp = s_temp + s_1

        for k in range(repeat_times):
            s_new += s_temp

        return i

    def decodeString(self,s):
        """
        :type s: str
        :rtype: str
        """
        s_new = []
        self.run_temp(s, 0, 1, s_new)
        s_new = ''.join(s_new)
        return s_new
