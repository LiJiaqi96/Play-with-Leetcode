class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if(len(x) < 4):
            return False
        else:
            x.extend([0,0])
            print(x)
            for i in range(2,len(x)-2):
                if(x[i] <= x[i-2]):
                    if(x[i-2] - x[i-4] > 0):
                        if(x[i] >= x[i-2] - x[i-4]):
                            if(x[i+1] != 0 and x[i+1] >= x[i-1] - x[i-3]):
                                return True
                            else:
                                pass
                        else:
                            if x[i+1] >= x[i-1]:
                                return True
                            else:
                                pass
                    else:
                        if x[i+1] >= x[i-1]:
                            return True
                        else:
                            pass
                else:
                    pass
            return False
