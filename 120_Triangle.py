class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if(len(triangle) == 0):
            return 0
        elif(len(triangle) == 1):
            return triangle[0][0]
        else:
            for i in range(1,len(triangle)):
                for j in range(len(triangle[i])):
                    if(j == 0):
                        left = None
                        right = triangle[i-1][j] + triangle[i][j]
                    elif(j == len(triangle[i])-1):
                        left = triangle[i-1][j-1] + triangle[i][j]
                        right = None
                    else:
                        left = triangle[i-1][j-1] + triangle[i][j]
                        right = triangle[i-1][j] + triangle[i][j]
                    if(left == None):
                        triangle[i][j] = right
                    elif(right == None):
                        triangle[i][j] = left
                    else:
                        triangle[i][j] = min(left,right)
        result = min(triangle[len(triangle)-1])
        return result
