class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n == 0):
            return False
        elif(n == 1):
            return True
        else:
            num = n
            meet_list = [num]
            temp_sum = self.cal_happy(num)
            if(temp_sum == 1):
                return True
            while(temp_sum != 1):
                if(temp_sum in meet_list):
                    return False
                temp_num = temp_sum
                meet_list.append(temp_sum)
                temp_sum = self.cal_happy(temp_num)         
            return True
                
                
    
    def cal_happy(self,number):
        num_list = list(str(number))
        sums = 0
        for i in range(len(num_list)):
            sums += int(num_list[i]) * int(num_list[i])
        return sums
