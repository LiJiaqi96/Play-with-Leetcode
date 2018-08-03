class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # initialize matrix
        matrix = [[0 for x in range(n)] for y in range(n)]
        
        direction = 'r'  # keeps track of which edge we're processing
        top = 0
        right = n
        bottom = n
        left = 0
        count = 0
				
        while count < n*n:
            if direction == 'r':
                for i in range(left, right):
                    count+=1
                    matrix[top][i] = count    
                top+=1
                direction = 'd'
                
            elif direction == 'd':
                for i in range(top, bottom):
                    count+=1
                    matrix[i][right-1] = count
                right -= 1
                direction = 'l'
                
            elif direction == 'l':
                for i in range(right-1, left-1, -1):
                    count+=1
                    matrix[bottom-1][i] = count
                bottom-=1
                direction = 'u'
                
            elif direction == 'u':
                for i in range(bottom-1, top-1, -1):
                    count+=1
                    matrix[i][left] = count
                
                left+=1
                direction = 'r'

        return matrix
        
