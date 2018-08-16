class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        matrix = [[0 for x in range(n)] for x in range(m)]    
        if(obstacleGrid[0][0] == 1):
            matrix[0][0] = 0
        else:
            matrix[0][0] = 1
        for i in range(1,m):
            if(obstacleGrid[i][0] == 1):
                matrix[i][0] = 0
            else:
                matrix[i][0] = matrix[i-1][0]
        for j in range(1,n):
            if(obstacleGrid[0][j] == 1):
                matrix[0][j] = 0
            else:
                matrix[0][j] = matrix[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j] == 1):
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        print(matrix)
        return matrix[m-1][n-1]
    
   
