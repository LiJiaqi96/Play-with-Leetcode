class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strs_list = list(s)
        length = len(strs_list)
        result = []
        for c1 in range(1,4):
            for c2 in range(1,4):
                for c3 in range(1,4):
                    for c4 in range(1,4):
                        if(c1 + c2 + c3 + c4 == length):
                            temp = []
                            flag = 1
                            num1 = int(''.join(strs_list[0:c1]))
                            num2 = int(''.join(strs_list[c1:c1+c2]))
                            num3 = int(''.join(strs_list[c1+c2:c1+c2+c3]))
                            num4 = int(''.join(strs_list[c1+c2+c3:c1+c2+c3+c4]))
                            if(num1 > 255 or num2 > 255 or num3 > 255 or num4 > 255):
                                flag = 0
                            elif(len(str(num1))!=len(strs_list[0:c1]) or len(str(num2))!=len(strs_list[c1:c1+c2]) or 
                         len(str(num3))!=len(strs_list[c1+c2:c1+c2+c3]) or len(str(num4))!=len(strs_list[c1+c2+c3:c1+c2+c3+c4])):
                                flag = 0
                            else:
                                pass
                            if(flag):
                                temp.append(str(num1))
                                temp.append(str(num2))
                                temp.append(str(num3))
                                temp.append(str(num4))
                                result.append('.'.join(temp))
                            else:
                                pass
                        else:
                            pass
        return result
