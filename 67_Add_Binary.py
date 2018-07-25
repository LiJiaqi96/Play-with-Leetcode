class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if(len(a) > len(b)):
            list1 = list(a)
            list2 = list(b)
        else:
            list1 = list(b)
            list2 = list(a)
        result = []
        # list1 refer to the longer one
        flag = 0
        for i in range(len(list1)):
            if(i < len(list2)):
                temp = int(list1[len(list1)-1-i]) + int(list2[len(list2)-1-i]) + flag
            else:
                temp = int(list1[len(list1)-1-i]) + flag
            if(temp >= 2):
                temp = temp - 2
                flag = 1
            else:
                flag = 0
            result = [str(temp)] + result
        if(flag):
            result = [str(flag)] + result
        else:
            pass
        return ''.join(result)

