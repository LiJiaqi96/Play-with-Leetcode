class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in range(len(nums)):
            if(dict.has_key(nums[i])):
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        for key, value in dict.items():
            if(value == 1):
                return key
