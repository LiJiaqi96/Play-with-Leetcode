class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp_matrix = [[0 for i in range(len(s))] for j in range(len(s))]

        begin = 0 
        length = 1 

        for i in range(len(s)):
            dp_matrix[i][i] = 1

        for i in range(len(s)-1):
            j = i + 1
            if(s[i] == s[j]):
                dp_matrix[i][j] = 1
                begin = i
                length = 2
            else:
                dp_matrix[i][j] = 0

        temp_length = 3
        while(temp_length <= len(s)):
            for i in range(len(s)-2):
                j = i + (temp_length - 1)
                if(j < len(s)): 
                    if(s[i] == s[j] and dp_matrix[i+1][j-1]):
                        dp_matrix[i][j] = 1
                        begin = i
                        length = temp_length 
                    else:
                        dp_matrix[i][j] = 0
            temp_length += 1

        solution = s[begin: begin + length]

        return solution
