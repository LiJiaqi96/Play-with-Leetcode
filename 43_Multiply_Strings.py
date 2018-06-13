class Solution(object):
    def calcu(self,n1,n2):
        multi_temp = []
        for i in range(len(n1)):
            single_multi = []
            add_num = 0
            flag = 0
            for j in range(len(n2)):
                temp = int(n1[len(n1)-1-i])*int(n2[len(n2)-1-j]) + add_num
                if(len(list(str(temp))) > 1):
                    add_num = int(list(str(temp))[0])    # Higher bit
                    lower_bit = int(list(str(temp))[1])
                else:
                    add_num = 0    # Higher bit
                    lower_bit = int(list(str(temp))[0])
                temp_num = lower_bit    # Lower bit
                if((lower_bit == 9) and flag):     # 9
                    temp_num = 0
                    flag = 1
                else:
                    if(flag):
                        temp_num += 1
                    else:
                        pass
                    flag = 0
                l = []
                l.append(temp_num)
                single_multi = l + single_multi    
            if(flag):
                single_multi = [add_num + 1] + single_multi    #  Cannot be higher than 9
            else:
                if(add_num == 0):
                    pass
                else:
                    single_multi = [add_num] + single_multi
            multi_temp.append(single_multi)
        return multi_temp

    def multiply(self,num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = list(num1)
        n2 = list(num2) 
        if(int(num1)==0 or int(num2)==0):
            return '0'    
        else:
            if(len(n1) <= len(n2)):
                # Set n1 as reference in multiplication
                result_temp = self.calcu(n1,n2)
            else:
                # Set n2 as reference in multiplication
                result_temp = self.calcu(n2,n1)
            std_length = len(result_temp)+len(result_temp[len(result_temp)-1])-1
            result_mid = []
            for i in range(std_length):
                temp = 0
                for j in range(len(result_temp)):
                    if((j-i > 0) or (i+1-j > len(result_temp[j]))):
                        pass
                    else:
                        temp += result_temp[j][len(result_temp[j])-1-(i-j)]
                result_mid.append(temp)    #  In reverse order
            result = []
            add_num = 0
            for k in range(len(result_mid)):
                middle = result_mid[k] + add_num
                if(len(list(str(middle))) > 1):
                    add_num = int(str(middle)[0:len(list(str(middle)))-1])
                    lower = int(list(str(middle))[len(list(str(middle)))-1])
                else:
                    add_num = 0
                    lower = int(list(str(middle))[0])
                l = []
                l.append(str(lower))
                result = l + result
            if(add_num):
                l = []
                l.append(str(add_num))
                result = l + result
            else:
                pass   
            result = ''.join(result)
            return result
