class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        new_board = [[0 for x in range(len(board[0]))] for y in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = self.live_nums(board,i,j)
                if(board[i][j] == 1 and num < 2):
                    new_board[i][j] = 0
                elif(board[i][j] == 1 and (num == 2 or num ==3)):
                    new_board[i][j] = 1
                elif(board[i][j] == 1 and num > 3):
                    new_board[i][j] = 0
                elif(board[i][j] == 0 and num == 3):
                    new_board[i][j] = 1
                else:
                    pass
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = new_board[i][j]
        '''no return, just modify board in-space'''
              
    def live_nums(self,board,i,j):
        if(len(board) == 1 or len(board[0]) == 1):
            return board
        elif(len(board) == 2 or len(board[0]) == 2):
            sums = 0
            for i in range(len(board)):
                sums += sum(board[i])
            return sums - board[i][j]
        else:
            if(i < 1):
                up,upleft,upright = 0,0,0
                if(j < 1):
                    left = 0
                    right = board[i][j+1]
                    downleft = 0
                    down = board[i+1][j]
                    downright = board[i+1][j+1]
                elif(j > len(board[0])-2):
                    left = board[i][j-1]
                    right = 0
                    downleft = board[i+1][j-1]
                    down = board[i+1][j]
                    downright = 0
                else:
                    left = board[i][j-1]
                    right = board[i][j+1]
                    downleft = board[i+1][j-1]
                    down = board[i+1][j]
                    downright = board[i+1][j+1]
            elif(i > len(board)-2):
                down,downleft,downright = 0,0,0      
                if(j < 1):
                    left = 0
                    right = board[i][j+1]
                    upleft = 0
                    up = board[i-1][j]
                    upright = board[i-1][j+1]
                elif(j > len(board[0])-2):
                    left = board[i][j-1]
                    right = 0
                    upleft = board[i-1][j-1]
                    up = board[i-1][j]
                    upright = 0
                else:
                    left = board[i][j-1]
                    right = board[i][j+1]
                    upleft = board[i-1][j-1]
                    up = board[i-1][j]
                    upright = board[i-1][j+1]
            else:
                if(j < 1):
                    left = 0
                    right = board[i][j+1]
                    upleft = 0
                    up = board[i-1][j]
                    upright = board[i-1][j+1]
                    downleft = 0
                    down = board[i+1][j]
                    downright = board[i+1][j+1]
                elif(j > len(board[0])-2):
                    left = board[i][j-1]
                    right = 0
                    upleft = board[i-1][j-1]
                    up = board[i-1][j]
                    upright = 0
                    downleft = board[i+1][j-1]
                    down = board[i+1][j]
                    downright = 0
                else:
                    left = board[i][j-1]
                    right = board[i][j+1]
                    upleft = board[i-1][j-1]
                    up = board[i-1][j]
                    upright = board[i-1][j+1] 
                    downleft = board[i+1][j-1]
                    down = board[i+1][j]
                    downright = board[i+1][j+1]
        return up+upright+right+downright+down+downleft+left+upleft
