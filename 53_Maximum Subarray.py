class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        else:
            temp = nums[0]
            sums = nums[0]
            for i in range(1,len(nums)):
                if(temp + nums[i] > nums[i]):
                    temp = temp + nums[i]
                else:
                    temp = nums[i]
                if(sums < temp):
                    sums = temp
                else:
                    pass
        return sums
