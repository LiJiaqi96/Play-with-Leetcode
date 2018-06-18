class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            return [nums]
        rotater = nums[0]
        new_sums = self.permute(nums[1:])
        for index in new_sums:
            for i in range(len(index)+1):
                result.append(index[0:i]+[rotater]+index[i:])
        return result
