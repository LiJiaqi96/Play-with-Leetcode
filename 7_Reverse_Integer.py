class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_list = list(str(x))
        num_new_list = []
        if(num_list[0] == '-'):
            neg = 1
        else:
            neg = 0
        for i in range(len(num_list)):
            num_new_list.append(num_list[len(num_list)-1-i])
        if(neg):
            num_new_list = num_new_list[:-1]
            num_new = int(''.join(num_new_list))
            if(num_new > 2**31):
                return 0
            else:
                return 0-num_new
        else:
            num_new = int(''.join(num_new_list))
            if(num_new > 2**31-1):
                return 0
            else:
                return num_new
