class Solution:
    def process(self,number):
        flag = 1
        number_new = number
        for i in range(len(number)):
            if((number[len(number)-1-i] == 9) and flag):
                number_new[len(number)-1-i] = 0
                flag = 1
            else:
                if(flag):
                    number_new[len(number)-1-i] += 1
                else:
                    pass
                flag = 0
        if(flag):
            number_new = [1] + number_new
        else:
            pass
        return number_new


    def plusOne(self,digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_new = digits
        if(digits[0] == 0):
            digits_new[0] += 1
        else:
            digits_new = self.process(digits)
        return digits_new
        
