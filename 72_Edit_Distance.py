class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lenght1, length2 = len(word1)-1, len(word2)-1
        dic = {}
        
        def change_times(index1, index2):
            if index1 == -1:
                return index2 + 1
            if index2 == -1:
                return index1 + 1
            if (index1,index2) in dic:
                return dic[(index1,index2)]
            if word1[index1] == word2[index2]:
                times = change_times(index1-1, index2-1)
            else:
                times = min(change_times(index1-1, index2-1), change_times(index1-1, index2), change_times(index1, index2-1)) + 1
            dic[(index1,index2)] = times
            return times
        result = change_times(lenght1,length2)
        
        return result
