class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        i = 0
        uplimit = len(tokens)
        temp = tokens[0]
        while(i < uplimit):
            if(tokens[i].isdigit() or len(tokens[i])>1):
                i += 1
            else:
                if(tokens[i] == '+'):
                    temp = int(tokens[i-2]) + int(tokens[i-1])
                elif(tokens[i] == '-'):
                    temp = int(tokens[i-2]) - int(tokens[i-1])
                elif(tokens[i] == '*'):
                    temp = int(tokens[i-2]) * int(tokens[i-1])
                else:
                    temp = int(int(tokens[i-2]) / int(tokens[i-1]))
                tokens[i] = str(temp)
                del(tokens[i-2:i])
                i -= 2
                uplimit -= 2
        return int(temp)
