class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in range(len(nums)):
            temp = []
            for index in result:
                temp.append(index + [nums[i]])
            result += temp
        return result
        
