class Solution(object):
    def iteration(self,n,num,rows,cols,final_rows,final_cols):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        search_fail = 1
        for i in range(n):
            if(i in cols):
                pass
            else:
                temp_flag = 1
                for j in range(len(rows)):
                    if(abs(num-rows[j]) == abs(i-cols[j])):
                        temp_flag = 0
                    else:
                        pass
                if(temp_flag):
                    search_fail = 0
                    rows.append(num)
                    cols.append(i)
                    if(n-1-num == 0):
                        final_rows.append(rows)
                        final_cols.append(cols)
                    else:
                        fail_flag,final_rows, final_cols = self.iteration(n,num+1,rows,cols,final_rows,final_cols)
                        if(fail_flag):
                            rows = rows[:-1]
                            cols = cols[:-1]
                        else:
                            pass
                else:
                    pass
        return search_fail,final_rows,final_cols
                      

    def solveNQueens(self,n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        chess = []
        if(n == 1):
            chess.append(['Q'])
        rows = []
        cols = []
        final_rows = []
        final_cols = []
        for i in range(n):
            rows = [0]
            cols = [i]
            fail_flag,final_rows,final_cols = self.iteration(n,1,rows,cols,final_rows,final_cols)
        for i in range(len(final_rows)):
            chess_temp = []
            for j in range(n):
                temp = ['.' for x in range(n)]
                temp[final_cols[i][j]] = 'Q'
                chess_temp.append(''.join(temp))
            chess.append(chess_temp)
        return chess
